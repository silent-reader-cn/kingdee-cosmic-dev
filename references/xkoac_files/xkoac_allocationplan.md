# 经营费用分摊方案-xkoac_allocationplan

## 经营费用分摊方案-主表 t_xkoac_allocationplan

- **表名称：** 经营费用分摊方案-主表
- **表名：** t_xkoac_allocationplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fdescribe | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 6 | fmaxrownum | 行编码最大号 | int4 | 32 |  | √ | 0 | 行编码最大号 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fenable | 禁用状态 | bpchar | 1 |  | √ | '1' | 禁用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fadvanceplan | 先行分摊方案 | int8 | 64 |  | √ | 0 | 经营费用分摊方案 xkoac_allocationplan |
| 16 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 17 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | faccountbook | 经营账簿 | int8 | 64 |  | √ | 0 | 经营账簿 xkoac_operatingbook |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_allocationplan |  | fid |
| 2 | idx_xkoac_allocationplan |  | fnumber |

---

## 经营组织架构版本-多选基础资料表 t_xkoac_orgstructure

- **表名称：** 经营组织架构版本-多选基础资料表
- **表名：** t_xkoac_orgstructure

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 经营组织架构版本 xkoac_orgsystem |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_orgstructure |  | fbasedataid |
| 2 | pk_xkoac_orgstructure |  | fpkid |

---

## 经营费用分摊方案-多语言表 t_xkoac_allocationplan_l

- **表名称：** 经营费用分摊方案-多语言表
- **表名：** t_xkoac_allocationplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fdescribe | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_allocationplan_l |  | fid,flocaleid |
| 2 | pk_xkoac_allocationplan_l |  | fpkid |

---

## 单据体-子表 t_xkoac_allocateentity

- **表名称：** 单据体-子表
- **表名：** t_xkoac_allocateentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsender | 发送方 | int8 | 64 |  | √ | 0 | 经营单元 xkoac_unit |
| 3 | frownumber | 行ID | int4 | 32 |  | √ | 0 | 行ID |
| 4 | ffilterlang | 过滤条件多语言 | varchar | 500 |  | √ | ' ' | 过滤条件多语言 |
| 5 | fallocateules | 分摊规则 | int8 | 64 |  | √ | 0 | 固定分摊权重 xkoac_shareweights |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffilter | 过滤条件设置 | varchar | 2000 |  | √ | ' ' | 过滤条件设置 |
| 8 | ffilterdesc | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | freceiveset | 接收方设置 | varchar | 200 |  | √ | ' ' | 接收方设置,枚举: 1 :取分摊目标设置的经营单元 2 :取发送方直接下级经营单元 3 :取发送方最底层经营单元 |
| 11 | fsourcebill | 来源单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_allocateentity |  | fentryid |
| 2 | idx_xkoac_allocateentity |  | fid |

---

## 分摊目标-子表 t_xkoac_allocatesub

- **表名称：** 分摊目标-子表
- **表名：** t_xkoac_allocatesub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freceiver | 接收方编码 | int8 | 64 |  | √ | 0 | 经营单元 xkoac_unit |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_allocatesub |  | fentryid |
| 2 | pk_xkoac_allocatesub |  | fdetailid |

---

## 单据体-多语言表 t_xkoac_allocateentity_l

- **表名称：** 单据体-多语言表
- **表名：** t_xkoac_allocateentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffilterlang | 过滤条件多语言 | varchar | 500 |  | √ | ' ' | 过滤条件多语言 |
| 2 | flocalieid | flocalieid | varchar | 10 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_allocateentity_l |  | fpkid |
| 2 | idx_xkoac_allocateentity_l |  | fentryid,flocalieid |
