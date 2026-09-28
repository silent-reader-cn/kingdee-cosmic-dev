# 投资资产价值变动台账-tccit_invest_asset_jzbd

## 投资资产价值变动台账-主表 t_tccit_invest_asset_jzbd

- **表名称：** 投资资产价值变动台账-主表
- **表名：** t_tccit_invest_asset_jzbd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 投资标的名称 | int8 | 64 |  | √ | 0 | 新增投资资产基础资料 tccit_new_invest_asset_bs |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | finvesttype | 投资性质 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fassettype | 资产类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 12 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fbillno | 资产编号 | varchar | 30 |  | √ | ' ' | 资产编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fassetstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: 0 :持有 1 :处置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_invest_asset_jzbd |  | fid |
| 2 | idx_tccit_invest_asset_jzbd |  | fbillno |

---

## 详细信息-子表 t_tccit_invest_jzbd_xx

- **表名称：** 详细信息-子表
- **表名：** t_tccit_invest_jzbd_xx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 3 | fdqwjrsydje | 其中：当期未计入损益的金额 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：当期未计入损益的金额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fjzbdtype | 价值变动类型 | varchar | 50 |  | √ | ' ' | 价值变动类型,枚举: 0 :公允价值变动 1 :资产减值 2 :损益调整 |
| 6 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | famount | 入账金额 | numeric | 23 | 10 | √ | 0.0000000000 | 入账金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbookedtime | 入账时间 | timestamp | 0 |  |  | null | 入账时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_invest_jzbd_xx_fk |  | fid |
| 2 | pk_tccit_invest_jzbd_xx |  | fentryid |
