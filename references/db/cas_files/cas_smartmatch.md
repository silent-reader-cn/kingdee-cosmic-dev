# 自动匹配业务单据规则-cas_smartmatch

## 自动匹配业务单据规则-主表 t_cas_smartmatch

- **表名称：** 自动匹配业务单据规则-主表
- **表名：** t_cas_smartmatch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | fautopay | 匹配后自动确认付款 | bpchar | 1 |  | √ | '0' | 匹配后自动确认付款 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 8 | forgid | 组织(历史数据) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fautorec | 匹配后收款单自动确认收款 | bpchar | 1 |  | √ | '0' | 匹配后收款单自动确认收款 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreateorg | fcreateorg | int8 | 64 |  | √ | 0 |  |
| 12 | fctrlstrategy | fctrlstrategy | varchar | 30 |  | √ | ' ' |  |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fbiztype | 匹配业务单据 | varchar | 30 |  | √ | ' ' | 匹配业务单据,枚举: rec :收款单 pay :付款单/同名转账 agentpay :报销/薪资付款单 transup :上划单 transdown :下拨单 transhandle :付款交易处理单 agentreturn :报销/薪资退款单 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 规则编码 | varchar | 30 |  | √ | ' ' | 规则编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_smartmatch_pkey |  | fid |
| 2 | idx_cas_smch_fnumber |  | fnumber |

---

## 适用组织-子表 t_cas_smartmatch_uorg

- **表名称：** 适用组织-子表
- **表名：** t_cas_smartmatch_uorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuorgid | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_smartmatch_uorg_pkey |  | fentryid |
| 2 | idx_cas_smartmatch_uorg |  | fuorgid |

---

## 匹配规则-子表 t_cas_smartmatch_e

- **表名称：** 匹配规则-子表
- **表名：** t_cas_smartmatch_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchplan | 关联规则 | varchar | 1024 |  | √ | ' ' | 关联规则 |
| 3 | fmatchplan_real | 匹配方案2 | text | 0 |  |  | null | 匹配方案2 |
| 4 | fbizcondition | 业务单据适用条件 | varchar | 1024 |  | √ | ' ' | 业务单据适用条件 |
| 5 | fmatchbyentry | 按分录匹配 | bpchar | 1 |  | √ | '0' | 按分录匹配 |
| 6 | fdcondition | 交易明细适用条件 | varchar | 1024 |  | √ | ' ' | 交易明细适用条件 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmultiple | 允许多个结果自动匹配 | bpchar | 1 |  | √ | '0' | 允许多个结果自动匹配 |
| 9 | fremarkt | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fdconditionreal | 交易明细适用条件real | text | 0 |  |  | null | 交易明细适用条件real |
| 11 | fisenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 12 | frulesname | 规则项名称 | varchar | 100 |  | √ | ' ' | 规则项名称 |
| 13 | fdconditionreal_tag | 交易明细适用条件real_详情 | text | 0 |  |  | null | 交易明细适用条件real_详情 |
| 14 | fbizconditionreal_tag | 业务单据适用条件real_详情 | text | 0 |  |  | null | 业务单据适用条件real_详情 |
| 15 | fmatchplan_real_tag | 匹配方案2_详情 | text | 0 |  |  | null | 匹配方案2_详情 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fbizconditionreal | 业务单据适用条件real | text | 0 |  |  | null | 业务单据适用条件real |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_smch_e |  | fid |
| 2 | t_cas_smartmatch_e_pkey |  | fentryid |

---

## 自动匹配业务单据规则-多语言表 t_cas_smartmatch_l

- **表名称：** 自动匹配业务单据规则-多语言表
- **表名：** t_cas_smartmatch_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 100 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_smartmatch_l_pkey |  | fpkid |
| 2 | idx_cas_smart_l |  | flocaleid,fid |
