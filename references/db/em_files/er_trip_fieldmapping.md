# 商旅字段映射-er_trip_fieldmapping

## 数据过滤-子表 t_er_trip_filterentry

- **表名称：** 数据过滤-子表
- **表名：** t_er_trip_filterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilterstatus | 状态 | varchar | 10 |  | √ | '1' | 状态,枚举: 1 :启用 0 :禁用 |
| 3 | ffilterfield | 字段 | varchar | 255 |  | √ | ' ' | 字段 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ffiltermodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | ffiltervalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 7 | ffilterleftbracket |  | varchar | 10 |  | √ | ' ' | ,枚举: ( :( |
| 8 | ffilterlogic |  | varchar | 10 |  | √ | ' ' | ,枚举: and :并且 or :或者 |
| 9 | ffilterrightbracket |  | varchar | 10 |  | √ | ' ' | ,枚举: ) :) |
| 10 | ffiltercreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 11 | ffilterisdefault | 是否系统预置 | varchar | 10 |  | √ | '0' | 是否系统预置 |
| 12 | ffilterdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | ffiltercondition | 条件 | varchar | 10 |  | √ | ' ' | 条件,枚举: = :等于 > :大于 < :小于 != :不等于 in :在集合中 is null :为空 is not null :不为空 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_filterentry_fid |  | fid |
| 2 | pk_t_er_trip_filterentry |  | fentryid |

---

## 商旅字段映射-主表 t_er_trip_fieldmapping

- **表名称：** 商旅字段映射-主表
- **表名：** t_er_trip_fieldmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 30 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fparamsjson_tag | 请求参数报文示例_详情 | text | 0 |  |  | ' ' | 请求参数报文示例_详情 |
| 5 | fparamsjson | 请求参数报文示例 | varchar | 255 |  | √ | ' ' | 请求参数报文示例 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmethod | 请求方式 | varchar | 50 |  | √ | ' ' | 请求方式,枚举: POST :POST GET :GET |
| 8 | fsynctype | 同步类型 | varchar | 10 |  | √ | ' ' | 同步类型,枚举: 1 :新增 2 :修改 |
| 9 | fdatajson | 返回数据报文示例 | varchar | 255 |  | √ | ' ' | 返回数据报文示例 |
| 10 | ffunction | 星翰对接功能 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | '1' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fserver | 服务商 | int8 | 64 |  | √ | 0 | 服务商设置 er_biz_info |
| 16 | fdatajson_tag | 返回数据报文示例_详情 | text | 0 |  |  | ' ' | 返回数据报文示例_详情 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | furl | 推送/拉取接口URL | varchar | 255 |  | √ | ' ' | 推送/拉取接口URL |
| 19 | fclassforname | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fporttype | 接口方式 | varchar | 30 |  | √ | ' ' | 接口方式,枚举: push :推送 pull :拉取 |
| 22 | fisdefault | 是否系统预置 | varchar | 2 |  | √ | '0' | 是否系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | uq_fieldmapping_fnumber |  | fnumber |
| 2 | pk_t_er_trip_fieldmapping |  | fid |
| 3 | idx_fieldmapping_fservice |  | fserver |

---

## 字段映射-子表 t_er_trip_fieldmapentry

- **表名称：** 字段映射-子表
- **表名：** t_er_trip_fieldmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmapsourcefield | 源单字段 | varchar | 255 |  | √ | ' ' | 源单字段 |
| 3 | fmaptargetfield | 目标单字段 | varchar | 255 |  | √ | ' ' | 目标单字段 |
| 4 | fmapdesignext | 计算公式/插件/常量/编码(二开) | varchar | 1000 |  | √ | ' ' | 计算公式/插件/常量/编码(二开) |
| 5 | fmapdesign | 计算公式/插件/常量/编码 | varchar | 1000 |  | √ | ' ' | 计算公式/插件/常量/编码 |
| 6 | fmapstatus | 状态 | varchar | 10 |  | √ | '1' | 状态,枚举: 1 :启用 0 :禁用 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmaptargetfielddesc | 目标单字段描述 | varchar | 1000 |  | √ | ' ' | 目标单字段描述 |
| 9 | fmaptypeext | 取值方式(二开) | varchar | 10 |  | √ | ' ' | 取值方式(二开),枚举: 1 :源单字段 2 :常量 3 :计算公式 4 :插件 5 :商旅字段映射编码 |
| 10 | fmapisdefault | 是否系统预置 | varchar | 10 |  | √ | '0' | 是否系统预置 |
| 11 | fmapcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fmapsourcefieldext | 源单字段(二开) | varchar | 255 |  | √ | ' ' | 源单字段(二开) |
| 13 | fmapmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 14 | fmaptype | 取值方式 | varchar | 10 |  | √ | ' ' | 取值方式,枚举: 1 :源单字段 2 :常量 3 :计算公式 4 :插件 5 :商旅字段映射编码 |
| 15 | fmapdesc | 描述 | varchar | 1000 |  | √ | ' ' | 描述 |
| 16 | fmapprimarykey | 主键 | varchar | 10 |  | √ | '0' | 主键 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_trip_fieldmapentry |  | fentryid |
| 2 | idx_fme_fid |  | fid |

---

## 查询条件-子表 t_er_trip_queryentry

- **表名称：** 查询条件-子表
- **表名：** t_er_trip_queryentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqueryleftbracket |  | varchar | 10 |  | √ | ' ' | ,枚举: ( :( |
| 3 | fquerydesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fquerystatus | 状态 | varchar | 10 |  | √ | '1' | 状态,枚举: 1 :启用 0 :禁用 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fquerypluginvalueext | 二开插件 | varchar | 255 |  | √ | ' ' | 二开插件 |
| 7 | fqueryrightbracket |  | varchar | 10 |  | √ | ' ' | ,枚举: ) :) |
| 8 | fquerycreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | fqueryfield | 字段 | varchar | 255 |  | √ | ' ' | 字段 |
| 10 | fqueryisdefault | 是否系统预置 | varchar | 10 |  | √ | '0' | 是否系统预置 |
| 11 | fquerylogic |  | varchar | 10 |  | √ | ' ' | ,枚举: and :并且 or :或者 |
| 12 | fquerymodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fquerycondition | 条件 | varchar | 30 |  | √ | ' ' | 条件,枚举: = :等于 > :大于 = :大于等于 <= :小于等于 != :不等于 in :在集合中 is null :为空 is not null :不为空 |
| 14 | fqueryvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fquerypluginvalue | 标准插件 | varchar | 255 |  | √ | ' ' | 标准插件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_queryentry_fid |  | fid |
| 2 | pk_t_er_trip_queryentry |  | fentryid |

---

## 可忽略异常-子表 t_er_trip_ignoreexentry

- **表名称：** 可忽略异常-子表
- **表名：** t_er_trip_ignoreexentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexfield | 字段 | varchar | 255 |  | √ | ' ' | 字段 |
| 3 | fexmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fexdesc | 异常描述 | varchar | 1000 |  | √ | ' ' | 异常描述 |
| 5 | fexisdefault | 是否系统预置 | varchar | 10 |  | √ | '0' | 是否系统预置 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fexcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fexnumber | 异常编码 | varchar | 255 |  | √ | ' ' | 异常编码 |
| 10 | fexstatus | 状态 | varchar | 10 |  | √ | '1' | 状态,枚举: 1 :启用 0 :禁用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ignoreexentry_fid |  | fid |
| 2 | pk_t_er_trip_ignoreexentry |  | fentryid |

---

## 商旅字段映射-多语言表 t_er_trip_fieldmapping_l

- **表名称：** 商旅字段映射-多语言表
- **表名：** t_er_trip_fieldmapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_trip_fieldmapping_l |  | fpkid |
| 2 | idx_fml_fidflocalid |  | fid,flocaleid |
