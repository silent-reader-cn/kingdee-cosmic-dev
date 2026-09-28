# 集成中间表-isc_buildmeta

## 集成中间表-主表 t_isc_buildmeta

- **表名称：** 集成中间表-主表
- **表名：** t_isc_buildmeta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 3 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fbizapp | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 6 | fbizunit | 功能分组 | varchar | 36 |  | √ | ' ' | 功能分组,枚举: |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: new :新建 update :待更新 success :已生成 |
| 11 | ftable_name | 表名 | varchar | 50 |  | √ | ' ' | 表名 |
| 12 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 13 | fentityid | 元数据id | varchar | 50 |  | √ | ' ' | 元数据id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_buildmeta |  | fid |
| 2 | idx_iscbuildmeta_num |  | fnumber |

---

## 集成中间表-多语言表 t_isc_buildmeta_l

- **表名称：** 集成中间表-多语言表
- **表名：** t_isc_buildmeta_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_buildmeta_l |  | fpkid |
| 2 | idx_iscbuildmetd_l |  | fid,flocaleid |

---

## 树形单据体-子表 t_isc_buildmeta_define

- **表名称：** 树形单据体-子表
- **表名：** t_isc_buildmeta_define

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffield_defvalue | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 3 | fisrequired | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 4 | ffield_type | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: varchar :字符串 time :日期 long :长整数 int :整数 decimal :小数 combo :下拉列表 checkbox :复选框 entries :分录 |
| 5 | ffield_desc | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 6 | ffield_info | 字段属性 | varchar | 255 |  | √ | ' ' | 字段属性 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftable_key | ftable_key | varchar | 50 |  | √ | ' ' |  |
| 9 | ftable_field | 表字段/分录表名 | varchar | 30 |  | √ | ' ' | 表字段/分录表名 |
| 10 | fshow_inlist | 是否在列表显示 | bpchar | 1 |  | √ | '0' | 是否在列表显示 |
| 11 | ffield_number | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 12 | finsearch | 是否支持快速过滤 | bpchar | 1 |  | √ | '0' | 是否支持快速过滤 |
| 13 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 14 | ffield_info_tag | 字段属性_详情 | text | 0 |  |  | null | 字段属性_详情 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_buildmeta_define |  | fentryid |
| 2 | idx_iscbuildmeta_define |  | fid,fentryid |
