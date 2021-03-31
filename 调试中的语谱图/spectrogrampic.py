#2-15行下面是运行成功的单独语音语谱图绘制
import matplotlib.pyplot as plt
import librosa.display

audio_path = 'D:/2020.03GitHub/pigcough/all/testsmall/clear.1.wav'
x , sr = librosa.load(audio_path)

X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
#plt.figure(figsize=(14, 5))
plt.figure(figsize=(2.27, 2.27), dpi=100)
#librosa.display.specshow(Xdb, cmap='plasma',sr=sr, x_axis='time', y_axis='hz')
librosa.display.specshow(Xdb, cmap='viridis')
#plt.ylim([0,4000])
#plt.colorbar()
plt.savefig('55noaxis.png')#默认保存地址？
#plt.show()

"""Python绘制语谱图"""
"""Python绘制时域波形"""

  # 导入相应的包
# import numpy, wave
# import matplotlib.pyplot as plt
# import numpy as np
# import os
# import matplotlib

#filepath = 'D:/2020.03GitHub/pigcough/all/testsmall/'  # 添加路径
# filename = os.listdir(filepath)  # 得到文件夹下的所有文件名

# #for i in range(len(filename)):
# for root, dirs, files in os.walk('D:/2020.03GitHub/pigcough/all/testsmall/'):
#     print("Root = ", root, "dirs = ", dirs, "files = ", files)
# for filename in files:
# #for i in range(len(filename)):
#     print (filename)
#     path_one = 'D:/2020.03GitHub/pigcough/all/testsmall/'+ filename
# #   f = wave.open(filepath + filename[i], 'rb')  # 调用wave模块中的open函数，打开语音文件。
#     f = wave.open(path_one,'rb')
#     params = f.getparams()  # 得到语音参数
#     nchannels, sampwidth, framerate, nframes = params[:4]  # nchannels:音频通道数，sampwidth:每个音频样本的字节数，framerate:采样率，nframes:音频采样点数
#     strData = f.readframes(nframes)  # 读取音频，字符串格式
#     wavaData = np.fromstring(strData, dtype=np.int16)  # 得到的数据是字符串，将字符串转为int型
#     wavaData = wavaData * 1.0/max(abs(wavaData))  # wave幅值归一化
#     wavaData = np.reshape(wavaData, [nframes, nchannels]).T  # .T 表示转置
#     f.close()
#
#      #（1）绘制语谱图
#     plt.figure()
#     plt.specgram(wavaData[0], Fs=framerate, scale_by_freq=True, sides='default')  # 绘制频谱
#     #plt.specgram(waveData, NFFT=512, Fs=44100, noverlap=384)
#     plt.xlabel('Time(s)')
#     plt.ylabel('Frequency')
#     #plt.title("Spectrogram_{}".format(i+1))
#     # plt.savefig('G:/实战培训/Python生成语谱图/语谱图/{}.jpg'.format(filename[i][:-4]))
#     plt.show()
 #    plt.specgram(waveData, NFFT=512, Fs=44100, noverlap=384)
 #    plt.axis('off')
 #    plt.axes().get_xaxis().set_visible(False)
 # #    plt.axes().get_yaxis().set_visible(False)
 #    fig = matplotlib.pyplot.gcf()
 #    if "."in filename:
 #        Filename = filename.split(".")[0]
 #    #plt.savefig(plotpath + Filename+'.jpg', dpi = 1200,bbox_inches = 'tight',pad_inches = 0)
 #    plt.savefig('D:/2020.03GitHub/pigcough/all/testsmall/' + Filename + '.jpg', dpi=1200, bbox_inches='tight', pad_inches=0)
    #plt.savefig('D:/2020.03GitHub/pigcough/all/testsmall/', dpi = 1200,bbox_inches = 'tight',pad_inches = 0)
 #    plt.clf()

