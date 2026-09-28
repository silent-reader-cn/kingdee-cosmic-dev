# 优质店铺-pmm_qualitystore

## 图片上传（废弃待删）-附件表 t_mal_compentry_fj

- **表名称：** 图片上传（废弃待删）-附件表
- **表名：** t_mal_compentry_fj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
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

## 组件分录-子表 t_mal_compentry

- **表名称：** 组件分录-子表
- **表名：** t_mal_compentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpic_desc | 图片描述 | varchar | 255 |  | √ | ' ' | 图片描述 |
| 3 | fgoodsid | fgoodsid | int8 | 64 |  | √ | 0 |  |
| 4 | ftag_color | 标签颜色 | varchar | 30 |  | √ | ' ' | 标签颜色 |
| 5 | fnotshowcategory | fnotshowcategory | bpchar | 1 |  | √ | '0' |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsource | fsource | varchar | 50 |  | √ | ' ' |  |
| 8 | fpicture | 上传图片 | varchar | 512 |  | √ | ' ' | 上传图片 |
| 9 | ftitle | ftitle | varchar | 50 |  | √ | ' ' |  |
| 10 | fselectmode | fselectmode | bpchar | 1 |  | √ | ' ' |  |
| 11 | fpic_title | 图片标题 | varchar | 100 |  | √ | ' ' | 图片标题 |
| 12 | finformation | finformation | varchar | 100 |  | √ | ' ' |  |
| 13 | furl | 链接地址 | varchar | 512 |  | √ | ' ' | 链接地址 |
| 14 | fcategoryid | fcategoryid | int8 | 64 |  | √ | 0 |  |
| 15 | fdesc_color | 描述颜色 | varchar | 30 |  | √ | ' ' | 描述颜色 |
| 16 | fentry_product_obtain_id | fentry_product_obtain_id | int8 | 64 |  | √ | 0 |  |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | ffont_color | 字体颜色 | varchar | 30 |  | √ | ' ' | 字体颜色 |

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

## 优质店铺-主表 t_mal_component

- **表名称：** 优质店铺-主表
- **表名：** t_mal_component

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 组件类型 | int8 | 64 |  | √ | 0 | [商城首页组件类型 pmm_compgroup](../pmm_files/pmm_compgroup.md) |
| 3 | fshow_way | fshow_way | varchar | 30 |  | √ | ' ' |  |
| 4 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmaxscrollnum | fmaxscrollnum | int8 | 64 |  | √ | 0 |  |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fscenarioschemeid | fscenarioschemeid | int8 | 64 |  | √ | 0 |  |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fvalid_date_end | fvalid_date_end | timestamp | 0 |  |  | null |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fvalid_date_start | fvalid_date_start | timestamp | 0 |  |  | null |  |
| 17 | fscenarioimage | fscenarioimage | varchar | 1000 |  | √ | ' ' |  |
| 18 | fisnew | 是否显示 | bpchar | 1 |  | √ | ' ' | 是否显示 |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 22 | fdelay | fdelay | int8 | 64 |  | √ | 0 |  |
| 23 | fcreatetime | 创建时间1 | timestamp | 0 |  |  | null | 创建时间1 |
| 24 | fpicture1 | fpicture1 | varchar | 500 |  | √ | ' ' |  |
| 25 | fproduct_obtain_id | fproduct_obtain_id | int8 | 64 |  | √ | 0 |  |
| 26 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 27 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 28 | fleftimg | 左侧主题图 | varchar | 500 |  | √ | ' ' | 左侧主题图 |
| 29 | fselectmode | fselectmode | bpchar | 1 |  | √ | ' ' |  |
| 30 | fspeed | fspeed | int8 | 64 |  | √ | 0 |  |
| 31 | fenable | 可用状态1 | bpchar | 1 |  | √ | ' ' | 可用状态1,枚举: 0 :禁用 1 :可用 |
| 32 | fisautoplay | fisautoplay | bpchar | 1 |  | √ | ' ' |  |
| 33 | fnumber | 组件编码 | varchar | 80 |  | √ | ' ' | 组件编码 |
| 34 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

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
| 4 | fdescription | 组件描述 | varchar | 255 |  | √ | ' ' | 组件描述 |
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
