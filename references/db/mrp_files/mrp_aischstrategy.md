# 智能排产策略-mrp_aischstrategy

## 单据体-子表 t_mrp_aistrategysty

- **表名称：** 单据体-子表
- **表名：** t_mrp_aistrategysty

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnum | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fcontent_tag | 内容_详情 | text | 0 |  |  | ' ' | 内容_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_aistrategysty |  | fid,fseq |
| 2 | pk_t_mrp_aistrategysty |  | fentryid |

---

## 智能排产策略-主表 t_mrp_aistrategy

- **表名称：** 智能排产策略-主表
- **表名：** t_mrp_aistrategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 策略名称 | varchar | 50 |  | √ | ' ' | 策略名称 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 策略编号 | varchar | 30 |  | √ | ' ' | 策略编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_aistrategy |  | fid |
| 2 | idx_mrp_aistrategy_bn |  | fbillno |

---

## 智能排产策略-多语言表 t_mrp_aistrategy_l

- **表名称：** 智能排产策略-多语言表
- **表名：** t_mrp_aistrategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 策略名称 | varchar | 100 |  | √ | ' ' | 策略名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_aistrategy_l |  | fid,flocaleid |
| 2 | pk_t_mrp_aistrategy_l |  | fpkid |

---

## 单据体-子表 t_mrp_aistrategyproty

- **表名称：** 单据体-子表
- **表名：** t_mrp_aistrategyproty

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnum | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fcontent_tag | 内容_详情 | text | 0 |  |  | ' ' | 内容_详情 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_aistrategyproty |  | fid,fseq |
| 2 | pk_t_mrp_aistrategyproty |  | fentryid |
