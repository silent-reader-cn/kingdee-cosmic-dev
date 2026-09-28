# 集成渠道类型-pbd_datachanneltype

## 集成渠道类型-多语言表 t_pbd_datachanneltype_l

- **表名称：** 集成渠道类型-多语言表
- **表名：** t_pbd_datachanneltype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 40 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_datachanneltype_l |  | fpkid |
| 2 | idx_pbd_datachanneltype_l |  | fid,flocaleid |

---

## 集成渠道类型-主表 t_pbd_datachanneltype

- **表名称：** 集成渠道类型-主表
- **表名：** t_pbd_datachanneltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fnumber | 类型编码 | varchar | 80 |  | √ | ' ' | 类型编码 |
| 8 | fjointsystemtype | 系统集成类型 | varchar | 50 |  | √ | ' ' | 系统集成类型,枚举: eas :eas self :self ierp :ierp xkcloud :xkcloud |
| 9 | fjointchannelfactoryclass | 默认集成渠道工厂类 | varchar | 255 |  | √ | ' ' | 默认集成渠道工厂类 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_datachanneltype |  | fid |
| 2 | idx_pbd_dct_fnumber |  | fnumber |
