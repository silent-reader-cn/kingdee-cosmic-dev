# 物理文件检查记录表-plmdc_physicalcheckrecord

## 物理文件检查记录表-主表 t_plmdc_physiccheckrecord

- **表名称：** 物理文件检查记录表-主表
- **表名：** t_plmdc_physiccheckrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuploadoption | 上传状态 | varchar | 50 |  | √ | ' ' | 上传状态,枚举: succeed :成功 fail :失败 |
| 3 | fphysical | 物理文件 | int8 | 64 |  | √ | 0 | [物理文件属性 plm_plmdc_physical_file](../plmdc_files/plm_plmdc_physical_file.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plmdc_physiccheckrecord |  | fid |
| 2 | idx_plmdc_physiccheckrecord |  | fphysical |
