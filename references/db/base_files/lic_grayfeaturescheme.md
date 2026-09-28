# 灰度特性-lic_grayfeaturescheme

## 灰度特性-主表 t_lic_grayfeaturescheme

- **表名称：** 灰度特性-主表
- **表名：** t_lic_grayfeaturescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdetailurl | 详情介绍链接 | varchar | 255 |  | √ | ' ' | 详情介绍链接 |
| 3 | fminversion | 依赖版本 | varchar | 80 |  | √ | ' ' | 依赖版本 |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fintroduction | 简介 | varchar | 1024 |  | √ | ' ' | 简介 |
| 6 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_grayfeaturescheme |  | fid |
| 2 | idx_lic_grayfeaturescheme_num |  | fnumber |

---

## 业务应用-子表 t_lic_grayfeatscheapp

- **表名称：** 业务应用-子表
- **表名：** t_lic_grayfeatscheapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisblack | 是否加入黑名单 | bpchar | 1 |  | √ | '1' | 是否加入黑名单 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fappnum | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 5 | fproduct | 产品标识码 | int8 | 64 |  | √ | 0 | 产品标识码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fappid | 业务应用名称 | varchar | 100 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lic_grayfeatscheapp_id |  | fid |
| 2 | pk_t_lic_grayfeatscheapp |  | fentryid |

---

## 业务云-子表 t_lic_grayfeatschecld

- **表名称：** 业务云-子表
- **表名：** t_lic_grayfeatschecld

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcloudnum | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 3 | fisblack | 是否加入黑名单 | bpchar | 1 |  | √ | '1' | 是否加入黑名单 |
| 4 | fcloudid | 业务云名称 | varchar | 100 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fproduct | 产品标识码 | int8 | 64 |  | √ | 0 | 产品标识码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_grayfeatschecld |  | fentryid |
| 2 | idx_lic_grayfeatschecld_id |  | fid |

---

## 业务对象-子表 t_lic_grayfeatscheobj

- **表名称：** 业务对象-子表
- **表名：** t_lic_grayfeatscheobj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentitynum | 业务对象编码 | varchar | 100 |  | √ | ' ' | 业务对象编码 |
| 3 | fisblack | 是否加入黑名单 | bpchar | 1 |  | √ | '1' | 是否加入黑名单 |
| 4 | fonsale | 是否上架 | bpchar | 1 |  | √ | '0' | 是否上架 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fappnum | 应用编码 | varchar | 100 |  | √ | ' ' | 应用编码 |
| 7 | fentityid | 业务对象名称 | varchar | 100 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fproduct | 产品标识码 | int8 | 64 |  | √ | 0 | 产品标识码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fappid | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lic_grayfeatscheobj |  | fentryid |
| 2 | idx_lic_grayfeatscheobj_id |  | fid |
