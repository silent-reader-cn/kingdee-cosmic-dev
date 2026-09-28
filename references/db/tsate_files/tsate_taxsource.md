# 税源管理-tsate_taxsource

## 税源管理-主表 t_tsate_taxsource

- **表名称：** 税源管理-主表
- **表名：** t_tsate_taxsource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginbw_tag | 通道商原始报文_详情 | text | 0 |  |  | null | 通道商原始报文_详情 |
| 3 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftakedate | 税源取得时间 | timestamp | 0 |  |  | null | 税源取得时间 |
| 5 | ftaxsourcetype | 税源类型 | int8 | 64 |  | √ | 0 | 税源类型 tpo_taxsourcetype |
| 6 | fdownloaddate | 税源下载时间 | timestamp | 0 |  |  | null | 税源下载时间 |
| 7 | fxzpc | 下载批次 | varchar | 50 |  | √ | ' ' | 下载批次 |
| 8 | fkdtaxsourcenumber | 税务云税源编号 | varchar | 50 |  | √ | ' ' | 税务云税源编号 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenddate | 纳税义务终止时间 | timestamp | 0 |  |  | null | 纳税义务终止时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsyzt | 税源状态 | varchar | 50 |  | √ | ' ' | 税源状态,枚举: 1 :正常 0 :义务终止 |
| 13 | foriginbw | 通道商原始报文 | varchar | 255 |  | √ | ' ' | 通道商原始报文 |
| 14 | fupdatestatus | 数据更新状态 | varchar | 50 |  | √ | '0' | 数据更新状态,枚举: 0 :未更新 1 :更新中 2 :更新成功 3 :更新失败 4 :无需更新 5 :新增成功 6 :新增失败 |
| 15 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 16 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 17 | fupdatedate | 税源更新时间 | timestamp | 0 |  |  | null | 税源更新时间 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fmaintaxoffice | 税源主管税务机关 | varchar | 100 |  | √ | ' ' | 税源主管税务机关 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | ftaxsourcename | 税局税源名称 | varchar | 50 |  | √ | ' ' | 税局税源名称 |
| 23 | fbw_tag | 税源报文_详情 | text | 0 |  |  | null | 税源报文_详情 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | ftaxsourcenumber | 税局税源编号 | varchar | 50 |  | √ | ' ' | 税局税源编号 |
| 26 | fdifferid | 最近一次比对记录id | varchar | 50 |  | √ | ' ' | 最近一次比对记录id |
| 27 | fbw | 税源报文 | varchar | 255 |  | √ | ' ' | 税源报文 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fdiffstatus | 差异比对结果 | varchar | 50 |  | √ | '0' | 差异比对结果,枚举: 0 :未比对 1 :比对中 2 :无差异 3 :有差异 4 :无比对数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_taxsource |  | fid |
| 2 | idx_tsate_taxsource1 |  | ftaxsourcenumber |
