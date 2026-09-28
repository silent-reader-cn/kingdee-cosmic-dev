# 资源包导出记录-isc_res_packages_export

## 单据体-子表 t_iscb_res_pkg_export_rr

- **表名称：** 单据体-子表
- **表名：** t_iscb_res_pkg_export_rr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | ftype | 资源类型 | varchar | 36 |  |  | ' ' | 业务对象 bos_objecttype |
| 4 | fsize | 大小（字节） | int8 | 64 |  | √ | 0 | 大小（字节） |
| 5 | fcontent_tag | 内容_详情 | text | 0 |  |  | ' ' | 内容_详情 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fres_pk | 资源ID | varchar | 50 |  |  | ' ' | 资源ID |
| 8 | fnumber | 编码 | varchar | 100 |  |  | ' ' | 编码 |
| 9 | fcontent | 内容 | varchar | 255 |  |  | ' ' | 内容 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fres_time | 最近修改时间 | timestamp | 0 |  |  | null | 最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iscb_res_pkg_export_rr |  | fentryid |
| 2 | idx_iscb_res_pkg_export_rr |  | fid |

---

## 资源包导出记录-主表 t_iscb_res_package_export

- **表名称：** 资源包导出记录-主表
- **表名：** t_iscb_res_package_export

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 资源信息 | varchar | 500 |  |  | ' ' | 资源信息 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fpackages | 资源包 | int8 | 64 |  | √ | 0 | 集成资源包 isc_res_packages |
| 7 | fbyte_count | 大小（字节） | int8 | 64 |  |  | null | 大小（字节） |
| 8 | fres_count | 主资源数 | int8 | 64 |  | √ | 0 | 主资源数 |
| 9 | fnumber | 批号 | varchar | 50 |  |  | ' ' | 批号 |
| 10 | fexport_time | 导出时间 | timestamp | 0 |  |  | null | 导出时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iscb_res_package_export |  | fid |
| 2 | idx_iscb_res_package_export |  | fpackages |

---

## 单据体-子表 t_iscb_res_pkg_export_mr

- **表名称：** 单据体-子表
- **表名：** t_iscb_res_pkg_export_mr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | fmain_export_content_tag | 实际导出内容(包含依赖)_详情 | text | 0 |  |  | ' ' | 实际导出内容(包含依赖)_详情 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fres_pk | 资源ID | varchar | 50 |  |  | ' ' | 资源ID |
| 6 | fmain_export_content | 实际导出内容(包含依赖) | varchar | 255 |  |  | ' ' | 实际导出内容(包含依赖) |
| 7 | ftype | 资源类型 | varchar | 36 |  |  | ' ' | 业务对象 bos_objecttype |
| 8 | fsize | 大小（字节） | int8 | 64 |  | √ | 0 | 大小（字节） |
| 9 | fcontent_tag | 内容_详情 | text | 0 |  |  | ' ' | 内容_详情 |
| 10 | fnumber | 编码 | varchar | 100 |  |  | ' ' | 编码 |
| 11 | fcontent | 内容 | varchar | 255 |  |  | ' ' | 内容 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fres_time | 最近修改时间 | timestamp | 0 |  |  | null | 最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_res_pkg_export_mr |  | fid |
| 2 | pk_iscb_res_pkg_export_mr |  | fentryid |
