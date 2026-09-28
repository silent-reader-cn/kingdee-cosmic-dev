# 许可控制清单-lic_licensegroupctrl

## 许可控制清单-主表 t_lic_licensegroupctrl

- **表名称：** 许可控制清单-主表
- **表名：** t_lic_licensegroupctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fgroupid | 许可分组 | int8 | 64 |  | √ | 0 | [许可分组 lic_group](../base_files/lic_group.md) |
| 4 | fbizobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fmoduleid | 许可模块 | int8 | 64 |  | √ | 0 | [许可模块 lic_module](../base_files/lic_module.md) |
| 6 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_lic_licensegroupctrl_obj |  | fbizobjectid |
| 2 | t_lic_licensegroupctrl_pkey |  | fid |
