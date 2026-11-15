import logging

class Header:
    dialSignature = b"HMDIAL\0"

    headerSize = 64
    unknownPos = 52
    parametersSizePos = 56

    def __init__(self, unknown, parametersSize):
        self.signature = Header.dialSignature
        self.modelMarker = 0x06
        self.unknown = unknown
        self.parametersSize = parametersSize


    def isValid(self):
        return self.signature == Header.dialSignature and self.modelMarker == 0x06


    def writeTo(self, stream):
        # verge-specific
        HeaderSize = 64
        buffer = bytearray(HeaderSize)
        for i in range(HeaderSize):
            buffer[i] = 0xff
        buffer[0:len(self.signature)] = self.signature
        buffer[11] = 0x06 # verge
        t = self.unknown.to_bytes(4, byteorder='little')
        buffer[52:52+len(t)] = t
        t = self.parametersSize.to_bytes(4, byteorder='little')
        buffer[56:56+len(t)] = t

        self.hackBuffer(buffer)
        stream.write(buffer)


    # from genuine watchfaces
    # don't know why yet
    def hackBuffer(self, buffer):
        p_0x10 = [0x20, 0x00, 0x6c, 0xea, 0x00, 0x00, 0x3f, 0x2c]
        for i in range(len(p_0x10)):
            buffer[0x10 + i] = p_0x10[i]
        # hard coding?
        buffer[60:60+4] = int(64).to_bytes(4, byteorder='little')


    @staticmethod
    def readFrom(stream):
        sig_buffer = stream.read(16)
        if len(sig_buffer) != 16:
            raise ValueError("Invalid or truncated Verge Lite watch-face header.")

        buffer = stream.read(64 - 16)
        if len(buffer) != 64 - 16:
            raise ValueError("Invalid or truncated Verge Lite watch-face header.")

        header = Header(
            unknown=int.from_bytes(buffer[52 - 16:56 - 16], byteorder="little"),
            parametersSize=int.from_bytes(buffer[56 - 16:60 - 16], byteorder="little"),
        )
        header.signature = sig_buffer[0:7]
        header.modelMarker = sig_buffer[0x0b]
        return header
