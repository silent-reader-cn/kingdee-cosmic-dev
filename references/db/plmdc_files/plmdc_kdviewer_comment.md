# 金蝶Viewer批注-plmdc_kdviewer_comment

## 金蝶Viewer批注-主表 t_plmdc_kdviewcomment

- **表名称：** 金蝶Viewer批注-主表
- **表名：** t_plmdc_kdviewcomment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fsprite | 元素 | varchar | 2000 |  | √ | ' ' | 元素 |
| 5 | fmainfileid | 轻量化文件 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |
| 6 | fflowno | 流程编码 | varchar | 400 |  | √ | ' ' | 流程编码 |
| 7 | fuuid | 唯一标识 | varchar | 50 |  | √ | ' ' | 唯一标识 |
| 8 | fcommentviewfileid | 批注视图文件 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |
| 9 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fcontent | 批注内容 | varchar | 2000 |  | √ | ' ' | 批注内容 |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_kdviewcomment |  | fid |
| 2 | idx_kdviewcomment_mainfile |  | fmainfileid |
