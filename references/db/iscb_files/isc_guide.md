# 集成方案（废弃）-isc_guide

## 集成方案（废弃）-多语言表 t_isc_guide_l

- **表名称：** 集成方案（废弃）-多语言表
- **表名：** t_isc_guide_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |
| 6 | fschedulename | fschedulename | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guide_l_fid |  | fid,flocaleid |
| 2 | t_isc_guide_l_pkey |  | fpkid |

---

## 数据规范表格-子表 t_isc_guide_showdata

- **表名称：** 数据规范表格-子表
- **表名：** t_isc_guide_showdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequired | 是否必填 | bpchar | 1 |  | √ | '0' | 是否必填 |
| 3 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础资料 6 :布尔值 7 :图片 8 :多选基础资料 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fentitypropalia | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | finterfield | 接口字段 | varchar | 100 |  | √ | ' ' | 接口字段 |
| 8 | ftextfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guidesd_fid |  | fid |
| 2 | t_isc_guide_showdata_pkey |  | fentryid |

---

## 数据反写表格-子表 t_isc_guide_reverse

- **表名称：** 数据反写表格-子表
- **表名：** t_isc_guide_reverse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperationtype | 操作类型 | int8 | 64 |  | √ | 0 | 操作类型,枚举: 1 :同步数据 2 :仅变更状态 3 :删除目标单据 |
| 3 | fpushtype | 推送类型 | int8 | 64 |  | √ | 1 | 推送类型,枚举: 0 :手动推送 1 :自动推送 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fregisterservice | 服务注册 | int8 | 64 |  | √ | 0 | 服务注册查询 isc_system_query |
| 6 | foperation | 操作 | varchar | 100 |  | √ | ' ' | 操作,枚举: |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guige_rever_fid |  | fid |
| 2 | t_isc_guide_reverse_pkey |  | fentryid |

---

## 分录映射表格-子表 t_isc_guide_entrymapping

- **表名称：** 分录映射表格-子表
- **表名：** t_isc_guide_entrymapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体名 | varchar | 100 |  | √ | ' ' | 实体名 |
| 3 | fentityalias | 实体别名 | varchar | 100 |  | √ | ' ' | 实体别名 |
| 4 | finterfacefield | 接口 | varchar | 100 |  | √ | ' ' | 接口 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryidentification | 分录标识 | varchar | 100 |  | √ | ' ' | 分录标识 |
| 7 | fentitytable | 表名 | varchar | 100 |  | √ | ' ' | 表名 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_guide_entrymapping_pkey |  | fentryid |
| 2 | idx_isc_guide_em_fid |  | fid |

---

## 分录4-子表 t_isc_guide_form_4

- **表名称：** 分录4-子表
- **表名：** t_isc_guide_form_4

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 13 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 14 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 17 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guidef_4_fid |  | fid |
| 2 | t_isc_guide_form_4_pkey |  | fentryid |

---

## 分录3-子表 t_isc_guide_form_3

- **表名称：** 分录3-子表
- **表名：** t_isc_guide_form_3

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 13 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 14 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 17 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_guide_form_3_pkey |  | fentryid |
| 2 | idx_isc_guidef_3_fid |  | fid |

---

## 分录6-子表 t_isc_guide_form_6

- **表名称：** 分录6-子表
- **表名：** t_isc_guide_form_6

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 13 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 14 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 17 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guide_f_6_fid |  | fid |
| 2 | t_isc_guide_form_6_pkey |  | fentryid |

---

## 分录5-子表 t_isc_guide_form_5

- **表名称：** 分录5-子表
- **表名：** t_isc_guide_form_5

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 13 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 14 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 17 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_guide_form_5_pkey |  | fentryid |
| 2 | idx_isc_guide_f_5_fid |  | fid |

---

## 单据头-子表 t_isc_guide_form_0

- **表名称：** 单据头-子表
- **表名：** t_isc_guide_form_0

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | funique | 唯一性标识 | bpchar | 1 |  | √ | '0' | 唯一性标识 |
| 13 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 14 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 15 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 18 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guidef_0_fid |  | fid |
| 2 | t_isc_guide_form_0_pkey |  | fentryid |

---

## 分录2-子表 t_isc_guide_form_2

- **表名称：** 分录2-子表
- **表名：** t_isc_guide_form_2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 13 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 14 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 17 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guidef_2_fid |  | fid |
| 2 | t_isc_guide_form_2_pkey |  | fentryid |

---

## 分录1-子表 t_isc_guide_form_1

- **表名称：** 分录1-子表
- **表名：** t_isc_guide_form_1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 13 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 14 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 17 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_guide_form_1_pkey |  | fentryid |
| 2 | idx_isc_guidef_1_fid |  | fid |

---

## 分录8-子表 t_isc_guide_form_8

- **表名称：** 分录8-子表
- **表名：** t_isc_guide_form_8

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 13 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 14 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 17 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guide_f_8_fid |  | fid |
| 2 | t_isc_guide_form_8_pkey |  | fentryid |

---

## 分录7-子表 t_isc_guide_form_7

- **表名称：** 分录7-子表
- **表名：** t_isc_guide_form_7

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 13 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 14 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 17 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_guide_form_7_pkey |  | fentryid |
| 2 | idx_isc_guide_f_7_fid |  | fid |

---

## 分录9-子表 t_isc_guide_form_9

- **表名称：** 分录9-子表
- **表名：** t_isc_guide_form_9

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpropfieldalias | 属性别名 | varchar | 100 |  | √ | ' ' | 属性别名 |
| 3 | fformat | 格式化表达式 | varchar | 100 |  | √ | ' ' | 格式化表达式 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fpropfield | 属性名称 | varchar | 100 |  | √ | ' ' | 属性名称 |
| 6 | fchangefield | 同步字段 | bpchar | 1 |  | √ | '0' | 同步字段 |
| 7 | fbdmappingid | 基础资料类型映射ID | varchar | 100 |  | √ | ' ' | 基础资料类型映射ID |
| 8 | frequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 9 | fdefault | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 10 | fuserdefined | 自定义字段 | bpchar | 1 |  | √ | '0' | 自定义字段 |
| 11 | fbdmapping | 基础资料映射 | int8 | 64 |  | √ | 0 | 基础资料映射（废弃） isc_basedatatype |
| 12 | ffieldtype | 字段类型 | varchar | 30 |  | √ | ' ' | 字段类型,枚举: 0 :字符 1 :数值 2 :日期 3 :枚举 4 :当前时间 5 :基础数据 6 :布尔值 7 :图片 8 :多选基础资料 |
| 13 | fexpfield | 公式 | varchar | 510 |  | √ | ' ' | 公式 |
| 14 | fbaseentityid | 基础资料ID | varchar | 100 |  | √ | ' ' | 基础资料ID |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | finterfield | 来源系统字段 | varchar | 200 |  | √ | ' ' | 来源系统字段 |
| 17 | fbaseentity | 基础资料 | varchar | 100 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_guide_form_9_pkey |  | fentryid |
| 2 | idx_isc_guide_f_9_fid |  | fid |

---

## 集成方案（废弃）-主表 t_isc_guide

- **表名称：** 集成方案（废弃）-主表
- **表名：** t_isc_guide

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finterfacename_1 | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 3 | finterfacename_2 | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 4 | fgroupid | 集成系统 | int8 | 64 |  | √ | 0 | 集成方案类别 isc_guidelefttree |
| 5 | finterfacename_3 | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 6 | finterfacename_4 | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 7 | finterfacename_5 | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 8 | finterfacename_6 | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 9 | finterfacename_7 | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 10 | fhandlerclass | 数据处理类： | varchar | 100 |  | √ | ' ' | 数据处理类： |
| 11 | finterfacename_8 | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 12 | finterfacename_9 | 接口名称 | varchar | 100 |  | √ | ' ' | 接口名称 |
| 13 | feasentity | 集成实体 | int8 | 64 |  | √ | 0 | 集成业务对象（废弃） isc_entity |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 17 | fbizcloud | 金蝶云苍穹业务云 | varchar | 80 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 20 | fmodifydate | fmodifydate | timestamp | 0 |  |  | null |  |
| 21 | flocalsystem | 目标系统 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |
| 22 | fcreater | fcreater | int8 | 64 |  | √ | 0 |  |
| 23 | fmqlinkscheme | MQ连接系统 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |
| 24 | fcustomeassolution | 通用接口服务名称 | varchar | 100 |  | √ | ' ' | 通用接口服务名称 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fbizapp | 金蝶云苍穹业务应用 | varchar | 80 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | frepushdata | 重复推送数据 | bpchar | 1 |  | √ | '0' | 重复推送数据 |
| 29 | fmodifier | fmodifier | int8 | 64 |  | √ | 0 |  |
| 30 | fdescription | fdescription | varchar | 100 |  | √ | ' ' |  |
| 31 | feassolution | 通用接口服务名称 | varchar | 100 |  | √ | ' ' | 通用接口服务名称,枚举: |
| 32 | fremotesystem | 源系统 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |
| 33 | fusemq | 是否使用MQ | int8 | 64 |  | √ | 1 | 是否使用MQ |
| 34 | fbasedatafield | 金蝶云苍穹实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 35 | fenable | 使用状态 | int8 | 64 |  | √ | 1 | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 37 | fvalueradio | 单选按钮组2 | int8 | 64 |  | √ | 0 | 单选按钮组2,枚举: 0 :字段为空时取默认值 1 :全取默认值 |
| 38 | ffiltercontext | 文本101 | text | 0 |  |  | null | 文本101 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_guide_fnum |  | fnumber |
| 2 | t_isc_guide_pkey |  | fid |
