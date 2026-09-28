# 取水量采集信息-tdm_water_resource

## 水资源纳税申报表B取水信息-子表 t_tdm_waterresource_entry

- **表名称：** 水资源纳税申报表B取水信息-子表
- **表名：** t_tdm_waterresource_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fzszm | 征收子目 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_szys_bizdef_entry |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fbqqslb | 本期取水量 | numeric | 23 | 10 | √ | 0 | 本期取水量 |
| 5 | fsqljqslb | 上期累计取水量 | numeric | 23 | 10 | √ | 0 | 上期累计取水量 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_waterresource_entry |  | fentryid |
| 2 | idx_tdm_waterresource_entry_fk |  | fid |

---

## 取水量采集信息-主表 t_tdm_water_resource

- **表名称：** 取水量采集信息-主表
- **表名：** t_tdm_water_resource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsbbbillstatus | 申报表单据状态 | varchar | 50 |  | √ | ' ' | 申报表单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fskssqq | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | ' ' | 申报状态,枚举: editing :未申报 declaring :申报中 declared :已申报 undeclare :未编制 declarefailed :申报失败 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsqljqsl | 上期累计取水量 | numeric | 23 | 10 | √ | 0 | 上期累计取水量 |
| 13 | fskssqz | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 14 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 申报表ID |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fsbbbillno | 申报表编号 | varchar | 50 |  | √ | ' ' | 申报表编号 |
| 17 | ftaxsourceid | 税源编号 | int8 | 64 |  | √ | 0 | [水资源税税源登记信息 tdm_water_source_dj](../tdm_files/tdm_water_source_dj.md) |
| 18 | fbqqsl | 本期取水量 | numeric | 23 | 10 | √ | 0 | 本期取水量 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_water_resource |  | fid |
| 2 | idx_tdm_water_resource_1 |  | forgid,fskssqq,fskssqz,fbillno |
