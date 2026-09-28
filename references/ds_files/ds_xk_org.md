# 星空组织中间表-ds_xk_org

## 星空组织中间表-主表 t_ds_xk_org

- **表名称：** 星空组织中间表-主表
- **表名：** t_ds_xk_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcreatetime | 星空创建时间 | timestamp | 0 |  |  | null | 星空创建时间 |
| 4 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 5 | fparentnumber | 上级组织编码 | varchar | 150 |  | √ | ' ' | 上级组织编码 |
| 6 | fparentname | 上级组织名称 | varchar | 150 |  | √ | ' ' | 上级组织名称 |
| 7 | fmodifytime | 星空修改时间 | timestamp | 0 |  |  | null | 星空修改时间 |
| 8 | forgpattern | 形态 | varchar | 50 |  | √ | ' ' | 形态,枚举: 101 :总公司 102 :公司 103 :工厂 104 :事业部 105 :分公司 106 :办事处 107 :部门 108 :其他 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :创建 B :审核中 C :已审核 D :待审核 Z :暂存 |
| 10 | fpolicy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略 |
| 11 | fparent | 上级组织 | varchar | 50 |  | √ | ' ' | 上级组织 |
| 12 | fenable | 禁用状态 | varchar | 50 |  | √ | ' ' | 禁用状态,枚举: A :否 B :是 |
| 13 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ds_xk_org |  | fnumber |
| 2 | pk_t_ds_xk_org |  | fid |
