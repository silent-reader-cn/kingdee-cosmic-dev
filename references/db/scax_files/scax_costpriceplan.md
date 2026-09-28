# 取价方案-scax_costpriceplan

## 产品委外标准价目表单据体-子表 t_scax_planoutpriceentry

- **表名称：** 产品委外标准价目表单据体-子表
- **表名：** t_scax_planoutpriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | foutprilevel | 取价优先级 | int4 | 32 |  | √ | 0 | 取价优先级 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | foutpriruleid | 取价规则 | int8 | 64 |  | √ | 0 | 取价规则 scax_costpricerule |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_planoutpriceentry |  | fid |
| 2 | pk_scax_planoutpriceentry |  | fentryid |

---

## 物料价目表单据体-子表 t_scax_planpurpricesentry

- **表名称：** 物料价目表单据体-子表
- **表名：** t_scax_planpurpricesentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurruleid | 取价规则 | int8 | 64 |  | √ | 0 | 取价规则 scax_costpricerule |
| 3 | fpurlevel | 取价优先级 | int4 | 32 |  | √ | 0 | 取价优先级 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_planpurpricesentry |  | fentryid |
| 2 | idx_scax_planpurpricesentry |  | fid |

---

## 取价方案-多语言表 t_scax_costpriceplan_l

- **表名称：** 取价方案-多语言表
- **表名：** t_scax_costpriceplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_costpriceplan_l |  | fpkid |
| 2 | idx_scax_costpriceplan_l |  | fid,flocaleid |

---

## 取价方案-主表 t_scax_costpriceplan

- **表名称：** 取价方案-主表
- **表名：** t_scax_costpriceplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbindbill | fbindbill | bpchar | 1 |  | √ | ' ' |  |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fdefaultplan | fdefaultplan | bpchar | 1 |  | √ | ' ' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scax_costpriceplan |  | fnumber |
| 2 | pk_scax_costpriceplan |  | fid |
