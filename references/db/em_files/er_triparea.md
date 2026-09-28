# 出差地域-er_triparea

## 出差地域明细-子表 t_er_tripareaentry

- **表名称：** 出差地域明细-子表
- **表名：** t_er_tripareaentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | fcomment | varchar | 255 |  |  | null |  |
| 3 | fcityid | 编码 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 4 | ftravelarea | ftravelarea | varchar | 255 |  |  | null |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fparentcityid | fparentcityid | int8 | 64 |  | √ | 0 |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_tae_fseq |  | fid,fseq |
| 2 | t_er_tripareaentry_pkey |  | fentryid |

---

## 国家或地区-多选基础资料表 t_er_triparea_country

- **表名称：** 国家或地区-多选基础资料表
- **表名：** t_er_triparea_country

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_area_country |  | fpkid |
| 2 | idx_er_area_country |  | fid |

---

## 出差地域-主表 t_er_triparea

- **表名称：** 出差地域-主表
- **表名：** t_er_triparea

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 5 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmulcombofield | 旺季 | varchar | 50 |  | √ | ' ' | 旺季,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 9 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 12 | fisinternational | 全球差旅 | bpchar | 1 |  | √ | '0' | 全球差旅 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 15 | fstatus | 数据状态 | varchar | 36 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fisothercity | 其他/任意城市 | bpchar | 1 |  | √ | '0' | 其他/任意城市 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fcitrystr | 城市字符串(废弃) | varchar | 255 |  | √ | ' ' | 城市字符串(废弃) |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_triparea_createorg |  | fcreateorgid |
| 2 | idx_t_er_triparea_master |  | fmasterid |
| 3 | idx_er_trar_fnumber |  | fnumber |
| 4 | t_er_triparea_pkey |  | fid |
| 5 | idx_er_trar_fcreateorgid |  | fcreateorgid |

---

## 城市F7-多选基础资料表 t_er_tripareacity

- **表名称：** 城市F7-多选基础资料表
- **表名：** t_er_tripareacity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_tripareacity_pkey |  | fpkid |
| 2 | idx_tparacity_fentryid |  | fentryid |

---

## 旺季区间-子表 t_er_tripareadateentry

- **表名称：** 旺季区间-子表
- **表名：** t_er_tripareadateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartday | 开始日期 | varchar | 50 |  | √ | '1' | 开始日期,枚举: 1 :1日 2 :2日 3 :3日 4 :4日 5 :5日 6 :6日 7 :7日 8 :8日 9 :9日 10 :10日 11 :11日 12 :12日 13 :13日 14 :14日 15 :15日 16 :16日 17 :17日 18 :18日 19 :19日 20 :20日 21 :21日 22 :22日 23 :23日 24 :24日 25 :25日 26 :26日 27 :27日 28 :28日 29 :29日 30 :30日 31 :31日 |
| 3 | fendday | 结束日期 | varchar | 50 |  | √ | '1' | 结束日期,枚举: 1 :1日 2 :2日 3 :3日 4 :4日 5 :5日 6 :6日 7 :7日 8 :8日 9 :9日 10 :10日 11 :11日 12 :12日 13 :13日 14 :14日 15 :15日 16 :16日 17 :17日 18 :18日 19 :19日 20 :20日 21 :21日 22 :22日 23 :23日 24 :24日 25 :25日 26 :26日 27 :27日 28 :28日 29 :29日 30 :30日 31 :31日 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fstartmonth | 开始月份 | varchar | 50 |  | √ | '1' | 开始月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 6 | fendmonth | 结束月份 | varchar | 50 |  | √ | '1' | 结束月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fid_tripareadateentry |  | fid |
| 2 | pk_t_er_tripareadateentry |  | fentryid |

---

## 城市F7-多选基础资料表 t_er_triparea_citys

- **表名称：** 城市F7-多选基础资料表
- **表名：** t_er_triparea_citys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_triparea_citys |  | fpkid |
| 2 | idx_tripareacitys_fid |  | fid |

---

## 出差地域-使用范围位图表 t_er_triparea_m

- **表名称：** 出差地域-使用范围位图表
- **表名：** t_er_triparea_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_triparea_m |  | forgid |

---

## 出差地域-多语言表 t_er_triparea_l

- **表名称：** 出差地域-多语言表
- **表名：** t_er_triparea_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_triparea_l_pkey |  | fpkid |
| 2 | idx_er_tarl_l_fid |  | fid,flocaleid |

---

## 出差地域-使用范围表 t_er_triparea_u

- **表名称：** 出差地域-使用范围表
- **表名：** t_er_triparea_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_triparea_u_uo |  | fuseorgid |
| 2 | t_er_triparea_u_pkey |  | fdataid,fuseorgid |
