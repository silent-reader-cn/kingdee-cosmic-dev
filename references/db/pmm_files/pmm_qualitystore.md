# 优质店铺-pmm_qualitystore

## 组件分录-子表 t_mal_compentry

- **表名称：** 组件分录-子表
- **表名：** t_mal_compentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpicture | 图片 | varchar | 512 |  | √ | ' ' | 图片 |
| 3 | ftitle | ftitle | varchar | 50 |  | √ | ' ' |  |
| 4 | fselectmode | fselectmode | bpchar | 1 |  | √ | ' ' |  |
| 5 | fgoodsid | fgoodsid | int8 | 64 |  | √ | 0 |  |
| 6 | finformation | finformation | varchar | 100 |  | √ | ' ' |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | furl | 链接地址 | varchar | 512 |  | √ | ' ' | 链接地址 |
| 9 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fsource | fsource | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_compentry |  | fentryid |
| 2 | idx_t_mal_compen_fgoods |  | fgoodsid |
| 3 | idx_t_mal_compen_fcat |  | fcategoryid |

---

## 优质店铺-多语言表 t_mal_component_l

- **表名称：** 优质店铺-多语言表
- **表名：** t_mal_component_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 组件名称 | varchar | 100 |  | √ | ' ' | 组件名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_comp_l_fid |  | fid |
| 2 | pk_mal_component_l |  | fpkid |

---

## 优质店铺-使用范围位图表 t_mal_component_m

- **表名称：** 优质店铺-使用范围位图表
- **表名：** t_mal_component_m

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
| 1 | pk_t_mal_component_m |  | forgid |

---

## 优质店铺-主表 t_mal_component

- **表名称：** 优质店铺-主表
- **表名：** t_mal_component

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 组件类型 | int8 | 64 |  | √ | 0 | 商城前端组件类型 pmm_compgroup |
| 3 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmaxscrollnum | fmaxscrollnum | int8 | 64 |  | √ | 0 |  |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fisnew | 是否显示 | bpchar | 1 |  | √ | ' ' | 是否显示 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 16 | fdelay | fdelay | int8 | 64 |  | √ | 0 |  |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 19 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 20 | fleftimg | 左侧主题图 | varchar | 500 |  | √ | ' ' | 左侧主题图 |
| 21 | fselectmode | fselectmode | bpchar | 1 |  | √ | ' ' |  |
| 22 | fspeed | fspeed | int8 | 64 |  | √ | 0 |  |
| 23 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fisautoplay | fisautoplay | bpchar | 1 |  | √ | ' ' |  |
| 25 | fnumber | 组件编码 | varchar | 80 |  | √ | ' ' | 组件编码 |
| 26 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_comp_fmast |  | fmasterid |
| 2 | idx_t_mal_component_master |  | fmasterid |
| 3 | pk_t_mal_component |  | fid |
| 4 | idx_t_mal_comp_fnum |  | fnumber |
| 5 | idx_t_mal_component_createorg |  | fcreateorgid |

---

## 图片上传-附件表 t_mal_compentry_fj

- **表名称：** 图片上传-附件表
- **表名：** t_mal_compentry_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_compentry_fj |  | fpkid |
| 2 | idx_t_mal_compen_fj_fid |  | fbasedataid |

---

## 优质店铺-使用范围表 t_mal_component_u

- **表名称：** 优质店铺-使用范围表
- **表名：** t_mal_component_u

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
| 1 | idx_t_mal_component_u_uo |  | fuseorgid |
| 2 | t_mal_component_u_pkey |  | fdataid,fuseorgid |
