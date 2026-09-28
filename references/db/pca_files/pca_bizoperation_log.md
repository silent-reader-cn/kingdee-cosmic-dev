# 项目成本执行日志-pca_bizoperation_log

## 项目成本执行日志-主表 t_pca_bizoperation_log

- **表名称：** 项目成本执行日志-主表
- **表名：** t_pca_bizoperation_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | flog_tag | 日志_详情 | text | 0 |  |  | ' ' | 日志_详情 |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbizoperation | 业务操作 | varchar | 100 |  | √ | ' ' | 业务操作,枚举: pca_projtimecoll :项目工时归集 pca_custallocrule :自定义分摊标准 pca_costalloc :项目公共费用分摊 pca_costunalloc :项目公共费用反分摊 pca_hoursdetail :项目人员工时归集 pca_laborcost_record :人工成本核算单归集 pca_cusalloc_std :自定义分摊标准获取数据 |
| 8 | flog | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: r :运行中 s :成功 f :失败 |
| 11 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 13 | fconsumetime | 耗时(毫秒) | int8 | 64 |  | √ | 0 | 耗时(毫秒) |
| 14 | fbillno | 日志编号 | varchar | 255 |  | √ | ' ' | 日志编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_bizoperation_log |  | fid |
| 2 | idx_pca_bizop_log0 |  | fbillno |
| 3 | idx_pca_bizop_log1 |  | fcostaccountid,fperiodid |
