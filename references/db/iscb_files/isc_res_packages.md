# 集成资源包-isc_res_packages

## 集成资源包-主表 t_iscb_res_packages

- **表名称：** 集成资源包-主表
- **表名：** t_iscb_res_packages

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  |  | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | ftag | 标签 | varchar | 50 |  |  | ' ' | 标签 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fres_count | 资源数 | int8 | 64 |  | √ | 0 | 资源数 |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iscb_res_packages |  | fid |
| 2 | idx_iscb_res_packages |  | fnumber |

---

## 资源列表-子表 t_iscb_res_packages_entry

- **表名称：** 资源列表-子表
- **表名：** t_iscb_res_packages_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fres_type | 资源类型 | varchar | 36 |  |  | ' ' | 业务对象 bos_objecttype |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fres_pk | 资源ID | varchar | 50 |  |  | ' ' | 资源ID |
| 5 | fres_name | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fres_number | 编码 | varchar | 100 |  |  | ' ' | 编码 |
| 8 | fres_time | 最近修改时间 | timestamp | 0 |  |  | null | 最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_res_packages_entry |  | fres_number |
| 2 | pk_iscb_res_packages_entry |  | fentryid |
