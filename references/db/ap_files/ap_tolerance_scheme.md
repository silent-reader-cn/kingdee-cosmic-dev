# 容差方案-ap_tolerance_scheme

## 容差方案-主表 t_ap_tolerance_scheme

- **表名称：** 容差方案-主表
- **表名：** t_ap_tolerance_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 9 | fcontrolpoint | 管控节点 | varchar | 50 |  | √ | ' ' | 管控节点,枚举: save :保存 submit :提交 audit :审核 |
| 10 | fcontrolmode | 管控方式按钮组 | varchar | 50 |  | √ | ' ' | 管控方式按钮组,枚举: WARN :超容提醒 FORBID :禁止超容 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_tolerance_scheme |  | fid |
| 2 | idx_ap_tol_scheme_status |  | fstatus |

---

## 容差方案-多语言表 t_ap_tolerance_scheme_l

- **表名称：** 容差方案-多语言表
- **表名：** t_ap_tolerance_scheme_l

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
| 1 | pk_t_ap_tolerance_scheme_l |  | fpkid |
| 2 | idx_ap_tol_scheme_l_fid |  | fid |

---

## 单据体-子表 t_ap_tolerance_scheme_d

- **表名称：** 单据体-子表
- **表名：** t_ap_tolerance_scheme_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fconditiondesc | 适用条件描述 | varchar | 2000 |  |  | null | 适用条件描述 |
| 4 | fmessage | 消息设置 | varchar | 2000 |  |  | null | 消息设置 |
| 5 | flowerlimit | 下限 | numeric | 23 | 10 | √ | 0.0000000000 | 下限 |
| 6 | ftolerancelimit | 容差限制 | varchar | 50 |  | √ | ' ' | 容差限制,枚举: PER :百分比 NUM :数值 |
| 7 | ftolerancestrategy | 容差策略 | int8 | 64 |  | √ | 0 | [容差策略 ap_tolerance_strategy](../ap_files/ap_tolerance_strategy.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fcondition | 适用条件 | varchar | 2000 |  |  | null | 适用条件 |
| 10 | fupperlimit | 上限 | numeric | 23 | 10 | √ | 0.0000000000 | 上限 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_tolerance_scheme_d |  | fentryid |
| 2 | idx_ap_tol_scheme_fid |  | fid |
