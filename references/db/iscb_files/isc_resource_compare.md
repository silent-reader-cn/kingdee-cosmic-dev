# 资源对比-isc_resource_compare

## 主资源-子表 t_iscb_res_comp_mr

- **表名称：** 主资源-子表
- **表名：** t_iscb_res_comp_mr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 资源名称 | varchar | 255 |  | √ | ' ' | 资源名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fres_pk | 资源ID | varchar | 50 |  | √ | ' ' | 资源ID |
| 6 | ftype | 资源类型 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | flocal_time | 本地最近修改时间 | timestamp | 0 |  |  | null | 本地最近修改时间 |
| 8 | fsize | 大小（字节） | int8 | 64 |  | √ | 0 | 大小（字节） |
| 9 | fcontent_tag | 资源内容_详情 | text | 0 |  |  | null | 资源内容_详情 |
| 10 | fnumber | 资源编码 | varchar | 255 |  | √ | ' ' | 资源编码 |
| 11 | fcontent | 资源内容 | varchar | 255 |  | √ | ' ' | 资源内容 |
| 12 | foperation | 模式 | varchar | 50 |  | √ | ' ' | 模式,枚举: INSERT :新增 UPDATE :更新 DELETE :不存在 IGNORE :忽略 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fres_time | 资源最近修改时间 | timestamp | 0 |  |  | null | 资源最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_res_comp_mr |  | fid |
| 2 | pk_t_iscb_res_comp_mr |  | fentryid |

---

## 引用资源-子表 t_iscb_res_comp_rr

- **表名称：** 引用资源-子表
- **表名：** t_iscb_res_comp_rr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 资源名称 | varchar | 255 |  | √ | ' ' | 资源名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fres_pk | 资源ID | varchar | 50 |  | √ | ' ' | 资源ID |
| 5 | ftype | 资源类型 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 6 | flocal_time | 本地最近修改时间 | timestamp | 0 |  |  | null | 本地最近修改时间 |
| 7 | fsize | 大小（字节） | int8 | 64 |  | √ | 0 | 大小（字节） |
| 8 | fcontent_tag | 资源内容_详情 | text | 0 |  |  | null | 资源内容_详情 |
| 9 | fnumber | 资源编码 | varchar | 255 |  | √ | ' ' | 资源编码 |
| 10 | fcontent | 资源内容 | varchar | 255 |  | √ | ' ' | 资源内容 |
| 11 | foperation | 模式 | varchar | 50 |  | √ | ' ' | 模式,枚举: INSERT :新增 UPDATE :更新 DELETE :不存在 IGNORE :忽略 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fres_time | 资源最近修改时间 | timestamp | 0 |  |  | null | 资源最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_res_comp_rr |  | fentryid |
| 2 | idx_iscb_res_comp_rr |  | fid |

---

## 资源对比-主表 t_iscb_res_comp

- **表名称：** 资源对比-主表
- **表名：** t_iscb_res_comp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fnumber | 任务编号 | varchar | 50 |  | √ | ' ' | 任务编号 |
| 7 | fprogress | 进度 | varchar | 50 |  | √ | ' ' | 进度,枚举: READY :暂存 COMPARING :对比中 COMPARED :对比完成 UPDATED :更新完成 UPDATE_FAILED :更新失败 |
| 8 | fsolution | 解决方案 | int8 | 64 |  | √ | 0 | 我的方案 isc_solution_center |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_res_comp_1 |  | fnumber |
| 2 | pk_t_iscb_res_comp |  | fid |
