# 功能分组-bos_devportal_bizunit

## 功能分组-多语言表 t_meta_bizunit_l

- **表名称：** 功能分组-多语言表
- **表名：** t_meta_bizunit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_bizunit_l_pkey |  | fpkid |
| 2 | idx_kdp_bizunit_localeid |  | fid,flocaleid |

---

## 功能分组-主表 t_meta_bizunit

- **表名称：** 功能分组-主表
- **表名：** t_meta_bizunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fisleaf | 是否有子节点 | bpchar | 1 |  | √ | '0' | 是否有子节点 |
| 3 | fparentid | 上级功能分组id | varchar | 36 |  | √ | ' ' | 上级功能分组id |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 254 | 序号 |
| 5 | fmodifier | 修改者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fdescription | fdescription | varchar | 500 |  | √ | ' ' |  |
| 7 | fparentname | 上级功能分组 | varchar | 50 |  | √ | ' ' | 上级功能分组 |
| 8 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 9 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | ftype | 类型 | varchar | 5 |  | √ | '1' | 类型,枚举: |
| 11 | fmasterid | 原厂功能分组id | varchar | 36 |  | √ | ' ' | 原厂功能分组id |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fcreater | 创建者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fparentpathid | 上级功能分组路径id | varchar | 36 |  | √ | ' ' | 上级功能分组路径id |
| 15 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_bizunit_pkey |  | fid |
| 2 | idx_kdp_bizunit_num |  | fnumber |
