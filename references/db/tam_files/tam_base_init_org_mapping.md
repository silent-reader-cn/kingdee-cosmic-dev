# 税务组织映射关系初始化-tam_base_init_org_mapping

## 税务组织映射关系初始化-主表 t_tam_base_init_org_map

- **表名称：** 税务组织映射关系初始化-主表
- **表名：** t_tam_base_init_org_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 完成状态 | varchar | 50 |  | √ | ' ' | 完成状态,枚举: 0 :未完成 1 :已完成 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fbasedataname | 资料名称 | varchar | 50 |  | √ | ' ' | 资料名称,枚举: mapping :税务组织映射关系 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fglysfa | 关联映射方案 | varchar | 500 |  | √ | ' ' | 关联映射方案 |
| 8 | ffetchtype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型,枚举: 0 :无需映射 1 :映射取数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tam_base_init_org_map |  | fid |
| 2 | idx_tam_base_init_org_map_1 |  | forgid |
