# 受控基础资料隐藏-xkbd_defctrlstrtgy_hide

## 受控基础资料隐藏-主表 t_xkbddefctrlstrtgy_hide

- **表名称：** 受控基础资料隐藏-主表
- **表名：** t_xkbddefctrlstrtgy_hide

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstatus | 数据状态 | varchar | 30 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbasedataid | 隐藏基础数据 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkbddefctrlstrtgy_hide |  | fbasedataid |
| 2 | pk_t_xkbddefctrlstrtgy_hide |  | fid |

---

## 受控基础资料隐藏-多语言表 t_xkbddefctrlstrtgy_hide_l

- **表名称：** 受控基础资料隐藏-多语言表
- **表名：** t_xkbddefctrlstrtgy_hide_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbddefctrlstrtgy_hide_l |  | fpkid |
| 2 | idx_xkbddefctrlstrtgy_hide_l_0 |  | fid,flocaleid |
