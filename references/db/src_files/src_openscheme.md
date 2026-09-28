# 开标管控方案-src_openscheme

## 开标管控方案-多语言表 t_src_openscheme_l

- **表名称：** 开标管控方案-多语言表
- **表名：** t_src_openscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 方案描述 | varchar | 500 |  | √ | ' ' | 方案描述 |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_openscheme_l |  | fpkid |
| 2 | idx_src_openscheme_l_fid |  | fid,flocaleid |

---

## 开标管控方案-主表 t_src_openscheme

- **表名称：** 开标管控方案-主表
- **表名：** t_src_openscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 3 | fissupautoencrypt | 是否自动进行加密 | bpchar | 1 |  | √ | '0' | 是否自动进行加密 |
| 4 | fsupdecryptpass | 供应商解密通过需要达到的条件 | bpchar | 1 |  | √ | '2' | 供应商解密通过需要达到的条件,枚举: 1 :至少有一个供应商解密 2 :一半以上供应商解密 3 :全部供应商均已解密 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fencryptnum | 参与加密最低人数要求 | int4 | 32 |  | √ | 0 | 参与加密最低人数要求 |
| 7 | fisopenbypkg | 是否需要按标段进行开标控制 | bpchar | 1 |  | √ | '0' | 是否需要按标段进行开标控制 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 10 | fbiztype | 开标类型 | varchar | 30 |  | √ | ' ' | 开标类型,枚举: 1 :开资审标 2 :开标/开技术标 3 :开商务标 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fisencryptbypkg | 是否需要按标段进行加解密控制 | bpchar | 1 |  | √ | '0' | 是否需要按标段进行加解密控制 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 15 | fremark | 方案描述 | varchar | 255 |  | √ | ' ' | 方案描述 |
| 16 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 17 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fdecryptpass | 解密通过需要达到的条件 | bpchar | 1 |  | √ | '3' | 解密通过需要达到的条件,枚举: 1 :至少有一个参与者解密 2 :一半以上参与者解密 3 :全部参与者均已解密 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fsupencryptnum | 参与加密最低供应商数要求 | int4 | 32 |  | √ | 0 | 参与加密最低供应商数要求 |
| 22 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fopennum | 参与开标最低人数要求 | int4 | 32 |  | √ | 0 | 参与开标最低人数要求 |
| 25 | fopenpass | 允许开标需要达到的条件 | bpchar | 1 |  | √ | '3' | 允许开标需要达到的条件,枚举: 1 :至少有一个开标人开标 2 :一半以上开标人开标 3 :全部开标人均已开标 |
| 26 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 27 | fisautoencrypt | 是否自动进行加密 | bpchar | 1 |  | √ | '0' | 是否自动进行加密 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_openscheme_num |  | fnumber |
| 2 | pk_src_openscheme |  | fid |

---

## 寻源流程-多选基础资料表 t_src_opensourceflow

- **表名称：** 寻源流程-多选基础资料表
- **表名：** t_src_opensourceflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_opensourceflow_bid |  | fbasedataid |
| 2 | pk_src_opensourceflow |  | fpkid |
| 3 | idx_src_opensourceflow_fid |  | fid |

---

## 加密人员角色-多选基础资料表 t_src_encryptrole

- **表名称：** 加密人员角色-多选基础资料表
- **表名：** t_src_encryptrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务角色 pds_bizrole](../pds_files/pds_bizrole.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_encryptrole |  | fpkid |
| 2 | idx_src_encryptrole |  | fid |
| 3 | idx_src_encryptrole_bid |  | fbasedataid |

---

## 开标人员角色-多选基础资料表 t_src_openrole

- **表名称：** 开标人员角色-多选基础资料表
- **表名：** t_src_openrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务角色 pds_bizrole](../pds_files/pds_bizrole.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_openrole_bid |  | fbasedataid |
| 2 | pk_src_openrole |  | fpkid |
| 3 | idx_src_openrole_fid |  | fid |

---

## 寻源方式-多选基础资料表 t_src_opensourcetype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_src_opensourcetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_opensourcetype |  | fpkid |
| 2 | idx_src_opensourcetype_bid |  | fbasedataid |
| 3 | idx_src_opensourcetype |  | fid |
