# 供需集市映射关系实体-sdm_mapping

## 用户映射明细-子表 t_sdm_mappingdetails

- **表名称：** 用户映射明细-子表
- **表名：** t_sdm_mappingdetails

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |
| 4 | fcredentials | 供需集市登录凭证 | varchar | 50 |  | √ | ' ' | 供需集市登录凭证 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsdmusername | 供需集市用户名 | varchar | 50 |  | √ | ' ' | 供需集市用户名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sdm_mappingdetails |  | fentryid |
| 2 | idx_sdm_mappingdetails_userid |  | fuserid |

---

## 供需集市映射关系实体-主表 t_sdm_mapping

- **表名称：** 供需集市映射关系实体-主表
- **表名：** t_sdm_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductid | 产品实例ID | varchar | 50 |  | √ | ' ' | 产品实例ID |
| 3 | fgroupname | 集团名称 | varchar | 255 |  | √ | ' ' | 集团名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sdm_mapping_productid |  | fproductid |
| 2 | pk_t_sdm_mapping |  | fid |
