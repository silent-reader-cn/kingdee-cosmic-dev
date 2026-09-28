# 实例-kf_instance

## 实例-主表 t_kf_instance

- **表名称：** 实例-主表
- **表名：** t_kf_instance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fgroupid | 分组ID | int8 | 64 |  | √ | 0 | 分组ID |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 6 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用列表 bos_devp_bizapplist |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 12 | fdata | 配置 | text | 0 |  |  | null | 配置 |
| 13 | fenabled | 状态 | bpchar | 1 |  | √ | '1' | 状态,枚举: 0 :禁用 1 :启用 |
| 14 | fversion | 版本 | int4 | 32 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kf_ins_number |  | fnumber |
| 2 | pk_t_kf_instance |  | fid |

---

## 实例-多语言表 t_kf_instance_l

- **表名称：** 实例-多语言表
- **表名：** t_kf_instance_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fdata | fdata | text | 0 |  |  | null |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kf_ins_l_fid |  | fid,flocaleid |
| 2 | pk_t_kf_instance_l |  | fpkid |
