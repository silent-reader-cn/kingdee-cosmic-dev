# 脚本片段模板-isc_script_example

## 脚本片段模板-多语言表 t_isc_script_example_l

- **表名称：** 脚本片段模板-多语言表
- **表名：** t_isc_script_example_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 脚本示例名称 | varchar | 100 |  | √ | ' ' | 脚本示例名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_script_example_l |  | fid,flocaleid |
| 2 | pk_t_isc_script_example_l |  | fpkid |

---

## 脚本片段模板-主表 t_isc_script_example

- **表名称：** 脚本片段模板-主表
- **表名：** t_isc_script_example

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 脚本示例名称 | varchar | 100 |  | √ | ' ' | 脚本示例名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [脚本片段模板分类 isc_script_scene](../iscb_files/isc_script_scene.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fscript_code_tag | 脚本_详情 | text | 0 |  |  | null | 脚本_详情 |
| 10 | fscript_code | 脚本 | varchar | 255 |  | √ | ' ' | 脚本 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_script_example |  | fid |
| 2 | idx_script_example_group |  | fgroupid |
