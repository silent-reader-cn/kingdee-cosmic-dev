# 隐私声明签署查询历史-userprivacystmthistory

## 隐私声明签署查询历史-主表 t_perm_userprivacystmt_h

- **表名称：** 隐私声明签署查询历史-主表
- **表名：** t_perm_userprivacystmt_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisagree | 是否同意 | bpchar | 1 |  | √ | '0' | 是否同意,枚举: 0 :未同意 1 :同意 2 :已撤销 |
| 3 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fprivacystmtid | 隐私声明 | int8 | 64 |  | √ | 0 | 隐私声明 privacystatement |
| 5 | fmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_userprivacystmt_h_pkey |  | fid |
| 2 | idx_userprivacystmt_h_user |  | fuserid |
