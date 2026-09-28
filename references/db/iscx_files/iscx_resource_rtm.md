# 资源配置（运行时）-iscx_resource_rtm

## 资源配置（运行时）-主表 t_iscx_res_main

- **表名称：** 资源配置（运行时）-主表
- **表名：** t_iscx_res_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | fcreator | int8 | 64 |  |  | null |  |
| 3 | fsourceapp | 来源应用 | varchar | 50 |  | √ | ' ' | 来源应用 |
| 4 | fdetails | 配置详情 | varchar | 255 |  |  | null | 配置详情 |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fdetails_tag | 配置详情_详情 | text | 0 |  |  | null | 配置详情_详情 |
| 7 | fmaintainer_tenant | 开发环境 | varchar | 100 |  |  | null | 开发环境 |
| 8 | fextensions_tag | 扩展配置_详情 | text | 0 |  |  | null | 扩展配置_详情 |
| 9 | fis_valid | fis_valid | bpchar | 1 |  |  | null |  |
| 10 | fextendor | fextendor | int8 | 64 |  |  | null |  |
| 11 | fversion | 版本号 | int8 | 64 |  |  | null | 版本号 |
| 12 | fremark | 备注 | varchar | 500 |  |  | null | 备注 |
| 13 | fname | 名称 | varchar | 500 |  |  | null | 名称 |
| 14 | fcatalog | 目录 | int8 | 64 |  |  | null | [资源目录 iscx_catalog](../iscx_files/iscx_catalog.md) |
| 15 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 16 | fis_extended | 是否已扩展 | bpchar | 1 |  |  | null | 是否已扩展 |
| 17 | fmodifier | fmodifier | int8 | 64 |  |  | null |  |
| 18 | fextendedtime | fextendedtime | timestamp | 0 |  |  | null |  |
| 19 | foutput_data_model_id | 输出数据模型ID | int8 | 64 |  | √ | 0 | 输出数据模型ID |
| 20 | ftype | 类型 | varchar | 36 |  |  | null | [资源类型 iscx_resource_type](../iscx_files/iscx_resource_type.md) |
| 21 | fext_tenant | fext_tenant | varchar | 50 |  |  | null |  |
| 22 | fnumber | 编码 | varchar | 150 |  |  | null | 编码 |
| 23 | fscope | 作用域 | int8 | 64 |  |  | null | [资源目录 iscx_catalog](../iscx_files/iscx_catalog.md) |
| 24 | fextensions | 扩展配置 | varchar | 255 |  |  | null | 扩展配置 |
| 25 | finput_data_model_id | 输入数据模型ID | int8 | 64 |  | √ | 0 | 输入数据模型ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscx_res_main_t |  | ftype |
| 2 | pk_t_iscx_res_main |  | fid |

---

## 资源配置（运行时）-多语言表 t_iscx_res_main_l

- **表名称：** 资源配置（运行时）-多语言表
- **表名：** t_iscx_res_main_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscx_res_main_l |  | fpkid |
| 2 | idx_iscx_res_main_l_n |  | fid,fname |
