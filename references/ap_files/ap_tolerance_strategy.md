# 容差策略-ap_tolerance_strategy

## 策略分录-子表 t_ap_tolerance_strategy_d

- **表名称：** 策略分录-子表
- **表名：** t_ap_tolerance_strategy_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontrolparty | 管控方 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | foppositeobjectdesc | 对比对象描述 | varchar | 2000 |  | √ | ' ' | 对比对象描述 |
| 5 | foppositeparty | 对比方 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | foppositeobject | 对比对象 | varchar | 50 |  | √ | ' ' | 对比对象 |
| 7 | fcontrolobjectdesc | 管控对象表达式 | varchar | 2000 |  | √ | ' ' | 管控对象表达式 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fcontrolobject | 管控对象 | varchar | 2000 |  | √ | ' ' | 管控对象 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fsource | 关系来源 | varchar | 50 |  | √ | ' ' | 关系来源,枚举: BOTP :BOTP CORE :核心单据行 SELF :本单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_tolerance_strategy_d |  | fentryid |
| 2 | idx_ap_tol_strategy_d_fid |  | fid |

---

## 容差策略-多语言表 t_ap_tolerance_strategy_l

- **表名称：** 容差策略-多语言表
- **表名：** t_ap_tolerance_strategy_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_tolerance_strategy_l |  | fpkid |
| 2 | idx_ap_tol_strategy_l_fid |  | fid |

---

## 容差策略-主表 t_ap_tolerance_strategy

- **表名称：** 容差策略-主表
- **表名：** t_ap_tolerance_strategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontrolparty | 管控方 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 11 | fisdefault | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_tol_strategy_status |  | fstatus |
| 2 | pk_t_ap_tolerance_strategy |  | fid |
