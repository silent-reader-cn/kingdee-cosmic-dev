# 共享中心组织分配-task_org

## 共享中心组织分配-多语言表 t_tk_org_l

- **表名称：** 共享中心组织分配-多语言表
- **表名：** t_tk_org_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  |  | null | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_org_l |  | fid,flocaleid |
| 2 | t_tk_org_l_pkey |  | fpkid |

---

## 共享中心组织分配-主表 t_tk_org

- **表名称：** 共享中心组织分配-主表
- **表名：** t_tk_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 4 | fimportorgid | 导入组织主键 | varchar | 100 |  | √ | ' ' | 导入组织主键 |
| 5 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 共享中心组织分配 task_org |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fssccenterid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 9 | forgtype | 组织类型 | int8 | 64 |  | √ | 0 | 组织视图方案 bos_org_viewschema |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | forgpattern | 形态 | varchar | 10 |  | √ | ' ' | 形态,枚举: 1 :公司 2 :分公司 3 :事业部 4 :部门 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_org_pkey |  | fid |
| 2 | index_ssc_org |  | fparentid |
