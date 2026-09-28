# 灰度许可控制清单-lic_graylicensegroupctrl

## 灰度许可控制清单-主表 t_lic_graylicgroupctrl

- **表名称：** 灰度许可控制清单-主表
- **表名：** t_lic_graylicgroupctrl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fbizobjectid | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fschemeid | 灰度特性方案 | int8 | 64 |  | √ | 0 | [灰度特性 lic_grayfeaturescheme](../base_files/lic_grayfeaturescheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lic_graylicgroupctrl_obj |  | fbizobjectid |
| 2 | pk_t_lic_graylicgroupctrl |  | fid |
