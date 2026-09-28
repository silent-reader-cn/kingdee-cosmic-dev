# 成本子要素与物料对应表-cad_subelement_material

## 成本子要素与物料对应表-主表 t_bd_subelement_material

- **表名称：** 成本子要素与物料对应表-主表
- **表名：** t_bd_subelement_material

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsubelementid | 子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 6 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 7 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_subelement_material_pkey |  | fid |
| 2 | index_bd_subelemat_fsbeleid |  | fsubelementid,fmaterialid |
