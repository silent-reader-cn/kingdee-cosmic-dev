# 归档记录查询-aef_acelre_con

## 归档记录查询-主表 t_aef_archive_log

- **表名称：** 归档记录查询-主表
- **表名：** t_aef_archive_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplication | 应用 | varchar | 30 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fcallbackfailreason | 档案系统失败原因 | varchar | 500 |  | √ | ' ' | 档案系统失败原因 |
| 4 | forgid | 归档组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ffilingid | 归档人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 状态 | varchar | 10 |  | √ | '0' | 状态,枚举: 0 :成功 1 :失败 2 :处理中 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | ffailreason | 失败原因 | varchar | 500 |  | √ | ' ' | 失败原因 |
| 10 | fbillno | 源单号码 | varchar | 30 |  | √ | ' ' | 源单号码 |
| 11 | fexetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | funiquekey | 唯一标识 | varchar | 100 |  | √ | ' ' | 唯一标识 |
| 16 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 17 | freason | 反归档原因 | varchar | 255 |  | √ | ' ' | 反归档原因 |
| 18 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 19 | fwayid | 方案 | int8 | 64 |  | √ | 0 | [归档方案 aef_archivescheme](../aef_files/aef_archivescheme.md) |
| 20 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 21 | fcallbackstatus | 档案系统状态 | varchar | 50 |  | √ | ' ' | 档案系统状态,枚举: 7004 :已正式归档 4001 :待整理 3003 :接收检测失败 2003 :接收入库失败 2103 :反归档成功 |
| 22 | ftype | 类型 | bpchar | 1 |  | √ | '0' | 类型,枚举: 1 :归档 2 :反归档 |
| 23 | fbillbizdate | 单据业务日期 | timestamp | 0 |  |  | null | 单据业务日期 |
| 24 | fbatchcode | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 25 | fuploadway | 上传方式 | varchar | 30 |  | √ | ' ' | 上传方式,枚举: 1 :道可维斯 2 :FTP 3 :发票云 4 :第三方档案系统 5 :电子档案云（共同部署） 6 :电子档案云（独立部署） |
| 26 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 27 | ffilingperiod | 归档期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 28 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aef_archive_log |  | fbillid,fbilltype |
| 2 | idx_org_book_bill_per_typ |  | forgid,ffilingperiod,fbilltype,fbooktypeid,ftype |
| 3 | t_aef_archive_log_pkey |  | fid |
