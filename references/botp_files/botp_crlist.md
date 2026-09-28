# 转换规则-botp_crlist

## 转换规则-分表 t_botp_convertrule_s

- **表名称：** 转换规则-分表
- **表名：** t_botp_convertrule_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fenabled | 启用状态 | bpchar | 1 |  | √ | '1' | 启用状态,枚举: 0 :已停用 1 :启用 |
| 3 | fisdefault | 默认规则 | bpchar | 1 |  | √ | '0' | 默认规则 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_botp_convertrule_s_pkey |  | fid |
| 2 | idx_botp_convertrule_s |  | fenabled |

---

## 转换规则-多语言表 t_botp_convertrule_l

- **表名称：** 转换规则-多语言表
- **表名：** t_botp_convertrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdata | fdata | text | 0 |  |  | null |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_botp_convertrule_l_pkey |  | fpkid |
| 2 | idx_botp_convertrule_fid |  | fid |

---

## 转换规则-主表 t_botp_convertrule

- **表名称：** 转换规则-主表
- **表名：** t_botp_convertrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 标识 | varchar | 36 |  | √ | ' ' | 标识 |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fsubsysid | fsubsysid | int8 | 64 |  |  | null |  |
| 4 | fmodeltype | fmodeltype | varchar | 50 |  |  | null |  |
| 5 | fparentid | fparentid | varchar | 36 |  |  | null |  |
| 6 | fisv | fisv | varchar | 50 |  |  | null |  |
| 7 | finheritpath | finheritpath | varchar | 300 |  | √ | ' ' |  |
| 8 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 9 | fsysstatus | 出厂状态 | bpchar | 1 |  | √ | '0' | 出厂状态,枚举: 0 :正常 1 :禁用 |
| 10 | fcreatedate | fcreatedate | timestamp | 0 |  | √ | LOCALTIMESTAMP |  |
| 11 | fmasterid | 原始规则 | varchar | 36 |  | √ | ' ' | 转换规则 botp_crlist |
| 12 | ftype | 扩展状态 | bpchar | 1 |  | √ | '0' | 扩展状态,枚举: 0 :原始规则 1 :派生规则 2 :扩展规则 |
| 13 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 14 | ftimestamp | ftimestamp | int8 | 64 |  |  | null |  |
| 15 | fenabled | fenabled | bpchar | 1 |  | √ | '1' |  |
| 16 | fdata | fdata | text | 0 |  |  | null |  |
| 17 | fsourceentitynumber | 源单 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 18 | fistemplate | fistemplate | bpchar | 1 |  |  | '0' |  |
| 19 | ftargetentitynumber | 目标单 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 20 | fversion | fversion | int8 | 64 |  | √ | 0 |  |
| 21 | fisdefault | fisdefault | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_botp_convertrule_pkey |  | fid |
| 2 | idx_botp_convertrule_src |  | fsourceentitynumber |
| 3 | idx_botp_convertrule_ms |  | fmasterid |
| 4 | idx_botp_convertrule_trg |  | ftargetentitynumber |
