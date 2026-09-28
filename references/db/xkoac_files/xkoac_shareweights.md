# 固定分摊权重-xkoac_shareweights

## 单据体-子表 t_xkoac_shareweightentry

- **表名称：** 单据体-子表
- **表名：** t_xkoac_shareweightentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbusunit | 经营单元编码 | int8 | 64 |  | √ | 0 | 经营单元 xkoac_unit |
| 3 | fweight | 权重值 | numeric | 23 | 10 | √ | 0 | 权重值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_shareweightentry |  | fentryid |
| 2 | idx_xkoac_shareweightentry |  | fid |

---

## 固定分摊权重-多语言表 t_xkoac_shareweights_l

- **表名称：** 固定分摊权重-多语言表
- **表名：** t_xkoac_shareweights_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_shareweights_l |  | fpkid |
| 2 | idx_xkoac_shareweights_l |  | fid,flocaleid |

---

## 固定分摊权重-主表 t_xkoac_shareweights

- **表名称：** 固定分摊权重-主表
- **表名：** t_xkoac_shareweights

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fallocaterules | 分摊规则 | bpchar | 1 |  | √ | '1' | 分摊规则,枚举: 2 :自定义分摊权重 1 :固定分摊权重 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fenable | 禁用状态 | bpchar | 1 |  | √ | '1' | 禁用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 15 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | faccountbook | 经营账簿 | int8 | 64 |  | √ | 0 | 经营账簿 xkoac_operatingbook |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_shareweights |  | fid |
| 2 | idx_xkoac_shareweights |  | fnumber |
