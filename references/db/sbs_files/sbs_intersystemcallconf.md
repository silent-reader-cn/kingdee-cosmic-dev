# 系统间联用配置-sbs_intersystemcallconf

## 系统间联用配置-主表 t_sbs_systemcallconf

- **表名称：** 系统间联用配置-主表
- **表名：** t_sbs_systemcallconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcommen | fcommen | varchar | 512 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcallsettings | fcallsettings | bpchar | 1 |  | √ | 'A' |  |
| 7 | fdescription | 参数描述 | varchar | 255 |  | √ | ' ' | 参数描述 |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_systemcallconf_fnumber |  | fnumber |
| 2 | pk_t_sbs_systemcallconf |  | fid |

---

## 系统间联用配置-多语言表 t_sbs_systemcallconf_l

- **表名称：** 系统间联用配置-多语言表
- **表名：** t_sbs_systemcallconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 参数描述 | varchar | 512 |  | √ | ' ' | 参数描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sbs_systemcallconf_l |  | fpkid |
| 2 | idx_fid_flocaleid |  | fid,flocaleid |
