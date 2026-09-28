# 税务归档记录查询-aef_acelre_tax

## 税务归档记录查询-主表 t_aef_archivetax_log

- **表名称：** 税务归档记录查询-主表
- **表名：** t_aef_archivetax_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplication | 应用 | varchar | 30 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fgroupid | 归档分组 | int8 | 64 |  | √ | 0 | [归档分组 aef_archivegroup](../aef_files/aef_archivegroup.md) |
| 4 | forgid | 归档组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ffilingid | 归档人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 状态 | varchar | 10 |  | √ | '0' | 状态,枚举: 0 :成功 1 :失败 2 :处理中 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fotherdata | 其他数据 | varchar | 255 |  | √ | ' ' | 其他数据 |
| 10 | ffailreason | 失败原因 | varchar | 500 |  | √ | ' ' | 失败原因 |
| 11 | fbillno | 源单号码 | varchar | 50 |  | √ | ' ' | 源单号码 |
| 12 | fotherdata_tag | 其他数据_详情 | text | 0 |  |  | null | 其他数据_详情 |
| 13 | fexetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | funiquekey | 唯一标识 | varchar | 100 |  | √ | ' ' | 唯一标识 |
| 18 | fskssqqdate | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | freason | 反归档原因 | varchar | 255 |  | √ | ' ' | 反归档原因 |
| 21 | ftaxarchivedata | 归档资料 | varchar | 50 |  | √ | ' ' | 归档资料,枚举: bill :单据 tccit :申报表 |
| 22 | fwayid | 方案 | int8 | 64 |  | √ | 0 | [归档方案 aef_archivescheme](../aef_files/aef_archivescheme.md) |
| 23 | fskssqzdate | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 24 | ftype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 1 :归档 2 :反归档 |
| 25 | fbillbizdate | 单据业务日期 | timestamp | 0 |  |  | null | 单据业务日期 |
| 26 | fbatchcode | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 27 | fuploadway | 上传方式 | varchar | 30 |  | √ | ' ' | 上传方式,枚举: 1 :道可维斯 2 :FTP 3 :发票云 |
| 28 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 29 | ffilingperiod | 期间 | varchar | 20 |  | √ | ' ' | 期间 |
| 30 | fbilltype | 单据类型 | varchar | 40 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aef_archivetax_log |  | fid |
| 2 | idx_aef_archivetax_log |  | fbillid,fbilltype |
| 3 | idx_org_per_bill_type |  | forgid,ffilingperiod,fbilltype,ftype |
