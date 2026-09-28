# CAD物料申请记录-plm_plmdc_cadapplymat

## CAD物料申请记录-主表 t_plmdc_cadapplymat

- **表名称：** CAD物料申请记录-主表
- **表名：** t_plmdc_cadapplymat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcadid | 图文档id | int8 | 64 |  | √ | 0 | 图文档id |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | funiquekey | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 5 | ffilename | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 6 | fmaterialid | 物料id | int8 | 64 |  | √ | 0 | 物料id |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmatapplyid | 物料申请单 | int8 | 64 |  | √ | 0 | 物料申请单 plm_pdm_compose_maf |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_cadapplymat |  | funiquekey |
| 2 | pk_t_plmdc_cadapplymat |  | fid |
