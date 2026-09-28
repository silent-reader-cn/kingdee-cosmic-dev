# 归档方式-pds_filemethod

## 归档方式-主表 t_pds_filemethod

- **表名称：** 归档方式-主表
- **表名：** t_pds_filemethod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fserverip | 服务器地址 | varchar | 50 |  | √ | ' ' | 服务器地址 |
| 8 | fpassword | 密码 | varchar | 50 |  | √ | ' ' | 密码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fpassword_enp | fpassword_enp | text | 0 |  |  | null |  |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fusername | 用户名 | varchar | 50 |  | √ | ' ' | 用户名 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftype | 归档类型 | bpchar | 1 |  | √ | '1' | 归档类型,枚举: 1 :苍穹文件服务器 |
| 16 | fisforbidden | fisforbidden | bpchar | 1 |  | √ | '0' |  |
| 17 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 19 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | fserverport | 端口 | varchar | 50 |  | √ | ' ' | 端口 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_filemethod_num |  | fnumber |
| 2 | idx_pds_filemethod_mid |  | fmasterid |
| 3 | pk_pds_filemethod |  | fid |

---

## 归档方式-多语言表 t_pds_filemethod_l

- **表名称：** 归档方式-多语言表
- **表名：** t_pds_filemethod_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_filemethod_l_fid |  | fid,flocaleid |
| 2 | pk_pds_filemethod_l |  | fpkid |
