# 我的盘点任务-fa_inventory_task

## 我的盘点任务-主表 t_fa_invent_taskrule

- **表名称：** 我的盘点任务-主表
- **表名：** t_fa_invent_taskrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsplitfieldvalue | 拆分依据字段 | varchar | 2000 |  |  | ' ' | 拆分依据字段 |
| 2 | finventperson | 盘点负责人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fentrystatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :未下达 B :已下达 C :已生成 |
| 4 | finventschemeid | 盘点方案id | int8 | 64 |  | √ | 0 | 盘点方案 fa_inventscheme_new |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 8 | fentryid | 盘点范围id | int8 | 64 |  | √ | 0 | 盘点范围(原我的盘点任务) fa_inventory_sope |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_invent_taskrule_pkey |  | fdetailid |
| 2 | idx_fa_invent_taskrule |  | fentryid |

---

## 盘点人-多选基础资料表 t_fa_invent_taskrule_chk

- **表名称：** 盘点人-多选基础资料表
- **表名：** t_fa_invent_taskrule_chk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_invent_taskrule_chk |  | fpkid |
| 2 | idx_fa_invent_tr_chk_fdetailid |  | fdetailid |

---

## 我的盘点任务-多语言表 t_fa_invent_taskrule_l

- **表名称：** 我的盘点任务-多语言表
- **表名：** t_fa_invent_taskrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_invent_taskrule_l_pkey |  | fpkid |
| 2 | idx_fa_invent_taskrule_l |  | fdetailid,flocaleid |
