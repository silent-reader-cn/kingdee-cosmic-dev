# 申报凭证-tsate_sbpz_admin

## 申报凭证-主表 t_tsate_sbpz_admin

- **表名称：** 申报凭证-主表
- **表名：** t_tsate_sbpz_admin

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 凭证名称 | varchar | 50 |  | √ | ' ' | 凭证名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbasedatasource | 数据来源 | int8 | 64 |  | √ | 0 | [申报通道 tsate_channel](../tsate_files/tsate_channel.md) |
| 8 | fdeclaretype | 申报表类型 | varchar | 50 |  | √ | ' ' | 模板类型 tpo_template_type |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fskssqq | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fskssqz | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 14 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fisarchive | 是否归档 | varchar | 50 |  | √ | '0' | 是否归档,枚举: 1 :是 0 :否 |
| 16 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :直连下载 0 :手工上传 |
| 17 | fsbqj | 申报期间 | timestamp | 0 |  |  | null | 申报期间 |
| 18 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 19 | fbillno | 凭证编号 | varchar | 30 |  | √ | ' ' | 凭证编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_sbpz_admin_fbillno |  | fbillno |
| 2 | pk_tsate_sbpz_admin |  | fid |
