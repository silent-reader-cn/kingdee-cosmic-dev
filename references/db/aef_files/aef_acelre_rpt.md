# 报表归档记录查询-aef_acelre_rpt

## 报表归档记录查询-主表 t_aef_acelre_rpt_log

- **表名称：** 报表归档记录查询-主表
- **表名：** t_aef_acelre_rpt_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ffilingid | 归档人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbcmorgid | fbcmorgid | int8 | 64 |  | √ | 0 |  |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 状态 | varchar | 10 |  | √ | '0' | 状态,枚举: 0 :成功 1 :失败 2 :处理中 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | ffailreason | 失败原因 | varchar | 500 |  | √ | ' ' | 失败原因 |
| 9 | fcurrentid | 单位 | int8 | 64 |  | √ | 0 | 金额单位 xkbd_amountunit |
| 10 | fbillno | 源单号码 | varchar | 80 |  | √ | ' ' | 源单号码 |
| 11 | fexetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | funiquekey | 唯一标识 | varchar | 100 |  | √ | ' ' | 唯一标识 |
| 16 | freportid | 报表 | varchar | 36 |  | √ | ' ' | 报表 xkrpt_report |
| 17 | fbcmtemplateid | fbcmtemplateid | int8 | 64 |  | √ | 0 |  |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | freason | 反归档原因 | varchar | 255 |  | √ | ' ' | 反归档原因 |
| 20 | fwayid | 方案 | int8 | 64 |  | √ | 0 | 归档方案 aef_archivescheme |
| 21 | fbcmfyid | fbcmfyid | int8 | 64 |  | √ | 0 |  |
| 22 | ftype | 类型 | bpchar | 1 |  | √ | '0' | 类型,枚举: 1 :归档 2 :反归档 |
| 23 | fbillbizdate | 单据业务日期 | timestamp | 0 |  |  | null | 单据业务日期 |
| 24 | fbcmsceneid | fbcmsceneid | int8 | 64 |  | √ | 0 |  |
| 25 | fbatchcode | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 26 | fuploadway | 上传方式 | varchar | 30 |  | √ | ' ' | 上传方式,枚举: 1 :道可维斯 2 :FTP 3 :发票云 |
| 27 | fyear | 年 | int8 | 64 |  | √ | 0 | 年 |
| 28 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 29 | fperiod | 期 | int8 | 64 |  | √ | 0 | 期 |
| 30 | fbcmperiodid | fbcmperiodid | int8 | 64 |  | √ | 0 |  |
| 31 | frpturl | 文件url | varchar | 2000 |  | √ | ' ' | 文件url |
| 32 | fcycleid | 周期 | varchar | 10 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 33 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aef_acelre_rpt_log |  | fid |
| 2 | idx_aef_archive_rpt_log |  | fbillid |
