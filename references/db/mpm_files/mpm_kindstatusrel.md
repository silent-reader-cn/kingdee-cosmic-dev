# 分类状态关系-mpm_kindstatusrel

## 分类状态关系-主表 t_mpm_kindstatrel

- **表名称：** 分类状态关系-主表
- **表名：** t_mpm_kindstatrel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | frelbizobjid | 关联业务对象 | varchar | 80 |  | √ | ' ' | 业务对象 bos_objecttype |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | 项目分类 bd_projectkind |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_kindstatrel_bilno |  | fbillno |
| 2 | pk_mpm_kindstatrel |  | fid |

---

## 单据体-子表 t_mpm_kindstatrelen

- **表名称：** 单据体-子表
- **表名：** t_mpm_kindstatrelen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstatustypeid | 状态类型 | varchar | 80 |  | √ | ' ' | 状态类型,枚举: bd_projectstatus :项目状态 mpm_taskstatus :任务状态 |
| 3 | fischange | 参与转换 | bpchar | 1 |  | √ | '0' | 参与转换 |
| 4 | fordernum | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fisstart | 开始状态 | bpchar | 1 |  | √ | '0' | 开始状态 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fstatusid | 状态 | int8 | 64 |  | √ | 0 | 项目状态 bd_projectstatus |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_kindstatrelen_fk |  | fid |
| 2 | pk_mpm_kindstatrelen |  | fentryid |
