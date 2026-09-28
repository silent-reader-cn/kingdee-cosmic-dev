# 经营费用分摊执行方案-xkoac_expensealloctplan

## 经营费用分摊执行方案-多语言表 t_xkoac_allctplan_l

- **表名称：** 经营费用分摊执行方案-多语言表
- **表名：** t_xkoac_allctplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fschemename | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_allctplan_l |  | fpkid |
| 2 | idx_xkoac_allctplan_l |  | fid,flocaleid |

---

## 经营费用分摊执行方案-主表 t_xkoac_allctplan

- **表名称：** 经营费用分摊执行方案-主表
- **表名：** t_xkoac_allctplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fschemename | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | frunall | 一键执行全部分摊方案 | bpchar | 1 |  | √ | '0' | 一键执行全部分摊方案 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fisshare | 是否共享 | bpchar | 1 |  | √ | '0' | 是否共享 |
| 8 | frunmode | 执行方式 | bpchar | 1 |  | √ | '0' | 执行方式,枚举: 0 :覆盖 1 :追加 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_allctplan |  | fid |
| 2 | idx_xkoac_allctplan |  | fcreatorid |

---

## 选择经营费用分摊方案-子表 t_xkoac_allctplansub

- **表名称：** 选择经营费用分摊方案-子表
- **表名：** t_xkoac_allctplansub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsourcescheme | 分摊方案编码 | int8 | 64 |  | √ | 0 | 经营费用分摊方案 xkoac_allocationplan |
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
| 1 | pk_xkoac_allctplansub |  | fdetailid |
| 2 | idx_xkoac_allctplansub |  | fentryid |

---

## 选择经营账簿-子表 t_xkoac_allctplanentity

- **表名称：** 选择经营账簿-子表
- **表名：** t_xkoac_allctplanentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fendperiod | 结束期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 3 | fstartperiod | 开始期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | foperatingbook | 经营账簿 | int8 | 64 |  | √ | 0 | 经营账簿 xkoac_operatingbook |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | forgsystem | 经营组织架构版本 | int8 | 64 |  | √ | 0 | 经营组织架构版本 xkoac_orgsystem |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_allctplanentity |  | fid |
| 2 | pk_xkoac_allctplanentity |  | fentryid |
