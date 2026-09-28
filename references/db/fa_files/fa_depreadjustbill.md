# 折旧调整-fa_depreadjustbill

## 折旧调整明细-子表 t_fa_depreadjustentry

- **表名称：** 折旧调整明细-子表
- **表名：** t_fa_depreadjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fbfrdepreamount | 调整前折旧 | numeric | 19 | 6 | √ | 0.000000 | 调整前折旧 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 7 | faftdepreamount | 调整后折旧 | numeric | 19 | 6 | √ | 0.000000 | 调整后折旧 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depreadjentry_rc |  | fid |
| 2 | t_fa_depreadjustentry_pkey |  | fentryid |

---

## 折旧调整-主表 t_fa_depreadjustbill

- **表名称：** 折旧调整-主表
- **表名：** t_fa_depreadjustbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fperiodid | 折旧期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 13 | fbillno | 调整单号 | varchar | 80 |  | √ | ' ' | 调整单号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depreadj_odp |  | forgid,fdepreuseid,fperiodid |
| 2 | idx_fa_depreadj_billno |  | fbillno |
| 3 | t_fa_depreadjustbill_pkey |  | fid |
