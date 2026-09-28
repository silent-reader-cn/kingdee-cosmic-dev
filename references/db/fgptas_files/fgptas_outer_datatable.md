# 外部数据表-fgptas_outer_datatable

## 外部数据表字段-多语言表 t_fgptas_otdtfield_l

- **表名称：** 外部数据表字段-多语言表
- **表名：** t_fgptas_otdtfield_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbfieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_otdtfield_l_0 |  | fid,flocaleid |
| 2 | pk_fgptas_otdtfield_l |  | fpkid |

---

## 外部数据表-多语言表 t_fgptas_outer_datatable_l

- **表名称：** 外部数据表-多语言表
- **表名：** t_fgptas_outer_datatable_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | idx_fgptas_outer_datatable_l_0 |  | fid,flocaleid |
| 2 | pk_fgptas_outer_datatable_l |  | fpkid |

---

## 外部数据表基本信息-多语言表 t_fgptas_otbasicinfo_l

- **表名称：** 外部数据表基本信息-多语言表
- **表名：** t_fgptas_otbasicinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasicname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_otbasicinfo_l_0 |  | fid,flocaleid |
| 2 | pk_fgptas_otbasicinfo_l |  | fpkid |

---

## 外部数据表字段-子表 t_fgptas_otdtfield

- **表名称：** 外部数据表字段-子表
- **表名：** t_fgptas_otdtfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbfieldfieldtp | 字段类型 | varchar | 10 |  | √ | ' ' | 字段类型,枚举: Text :文本 Integer :数值 Date :日期 |
| 3 | ftbfieldcreatetp | 创建方式 | varchar | 10 |  | √ | ' ' | 创建方式,枚举: 1 :导入 2 :手动新增 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ftbfieldname | 字段名称 | varchar | 60 |  | √ | ' ' | 字段名称 |
| 6 | ftbfieldnumber | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fgptas_otdtfield |  | fentryid |
| 2 | idx_fgptas_otdtfield_fk |  | fid |

---

## 外部数据表-主表 t_fgptas_outer_datatable

- **表名称：** 外部数据表-主表
- **表名：** t_fgptas_outer_datatable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 60 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fdescribe | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | frelationentityinfo | 关联实体信息JSON | varchar | 255 |  | √ | '{}' | 关联实体信息JSON |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_outer_datatable_m0 |  | fmasterid |
| 2 | pk_fgptas_outer_datatable |  | fid |

---

## 外部数据表基本信息-子表 t_fgptas_otbasicinfo

- **表名称：** 外部数据表基本信息-子表
- **表名：** t_fgptas_otbasicinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasicnumber | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 3 | fbasicname | 字段名称 | varchar | 60 |  | √ | ' ' | 字段名称 |
| 4 | fbasicfieldtp | 字段类型 | varchar | 10 |  | √ | ' ' | 字段类型,枚举: Basedata :基础资料 |
| 5 | fbasicmustinput | 必录 | bpchar | 1 |  | √ | '1' | 必录 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbasiccreatetp | 创建方式 | varchar | 10 |  | √ | ' ' | 创建方式,枚举: 1 :系统预置 2 :手动新增 |
| 8 | fbasicbdentitynum | 值来源 | varchar | 60 |  | √ | '{}' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 9 | fbasicdisplay | 显示 | bpchar | 1 |  | √ | '1' | 显示 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_otbasicinfo_fk |  | fid |
| 2 | pk_fgptas_otbasicinfo |  | fentryid |
